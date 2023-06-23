#math/viz
import numpy as np
from astropy.table import Table
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sys
from collections import OrderedDict
import math
from tqdm import tqdm
from matplotlib import rcParams

#ML Libraries
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torch.utils.data import DataLoader, Dataset
from tabgan.sampler import GANGenerator


#data processing
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from imblearn.combine import SMOTETomek
from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import confusion_matrix
import itertools




def read_data():
    #get black hole data from popsycle dataset
    pops = Table.read("data/popsycle_sim.fits").to_pandas()
    ob = Table.read("data/OB110462_DW_post.fits").to_pandas()
    print("data read")

    for i in range(len(pops)):
        if (pops["mass_L"][i] < 6 and pops["mass_L"][i] > 2 and (pops["rem_id_L"][i] == 103)):
            print(f'{pops["mass_L"][i]}, {pops["rem_id_L"][i]}')
        else:
            pops = pops.drop([i])

    pops.reset_index(inplace=True)
    pops = pops.drop(columns=["index"])

    wanted_ob = ["t0","u0_amp","tE","log10_thetaE","piE_E","muS_E","mL","piRel","muL_E","muRel_E"]
    wanted_pops = ["t0","u0","t_E","theta_E","pi_E","mu_b_S","mass_L","pi_rel","mu_b_L","mu_rel"]

    ob_to_pops = {"t0":"t0", "u0_amp":"u0","tE":"t_E","log10_thetaE":"theta_E","piE_E":"pi_E","muS_E":"mu_b_S","mL":"mass_L","piRel":"pi_rel","muL_E":"mu_b_L","muRel_E":"mu_rel"}
    print("Initial Data Augmentation")
    
    for col in [i for i in ob.columns]:
        if col in wanted_ob:
            pass
        else:
            ob = ob.drop(columns=[col])

    for col in [i for i in pops.columns]:
        if col in wanted_pops:
            pass
        else:
            pops = pops.drop(columns=[col])

    ob = ob.rename(columns=ob_to_pops, errors="raise")

    ob_targets = {"target":[1 for i in range(len(ob))]}
    pops_targets = {"target":[0 for i in range(len(pops))]}
    target_ob = pd.DataFrame(ob_targets)
    target_pops = pd.DataFrame(pops_targets)

    return ob, pops, target_ob, target_pops



def generate_CTGan():
    ob, pops, target_ob, target_pops = read_data()
    
    df_ob_ns_no_target = pd.concat([ob, pops], ignore_index=True)
    df_ob_ns_only_target = pd.concat([target_ob,target_pops], ignore_index=True)
    df_data_not_norm = pd.concat([df_ob_ns_no_target,df_ob_ns_only_target], axis=1)

    norm_bh_ns = preprocessing.Normalizer()
    df = norm_bh_ns.fit_transform(df_ob_ns_no_target)

    #smote tomek resample
    print("smote resample occuring")
    smk = SMOTETomek()
    X,y = smk.fit_resample(df, df_ob_ns_only_target.to_numpy())

    #split data for ctgan training
    df_x_train, df_x_test, df_y_train, df_y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        #shuffle=False,
        random_state=42,
    )
    df_xtrain = pd.DataFrame(df_x_train, columns=df_ob_ns_no_target.columns).reset_index(drop=True)
    df_xtest = pd.DataFrame(df_x_test, columns=df_ob_ns_no_target.columns).reset_index(drop=True)
    df_ytrain = pd.DataFrame(df_y_train, columns=["id"]).reset_index(drop=True)
    df_ytest = pd.DataFrame(df_y_test, columns=["id"]).reset_index(drop=True)

    #train ctgan
    print("ctgan training:")
    gen_x, gen_y = GANGenerator(
        gen_x_times=1.1, 
        cat_cols=None,
        bot_filter_quantile=0.001, 
        top_filter_quantile=0.999,
        is_post_process=True,
        adversarial_model_params={
            "metrics": "rmse", 
            "max_depth": 2, 
            "max_bin": 100, 
            "learning_rate": 0.02, 
            "random_state": 42, 
            "n_estimators": 500,
        }, 
        pregeneration_frac=2, 
        only_generated_data=False,
        gan_params = {
            "batch_size": 500, 
            "patience": 25, 
            "epochs" : 20,
        }).generate_data_pipe(
            df_xtrain, 
            df_ytrain,
            df_xtest, 
            deep_copy=True, 
            only_adversarial=False,
            use_adversarial=True
            )

    #combine real world data and ctgan synthetic data
    t = pd.concat([df_ob_ns_no_target,gen_x])
    f = pd.concat([df_ob_ns_only_target,pd.DataFrame(gen_y.to_numpy(),columns=["target"])])
    return pd.concat([t,f], axis=1).reset_index(drop=True)