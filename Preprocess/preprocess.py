import numpy as np
from astropy.table import Table
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from imblearn.combine import SMOTETomek


pops = Table.read("data/research_paper/popsycle_sim.fits").to_pandas()
ob = Table.read("data/research_paper/OB110462_DW_post.fits").to_pandas() #color data

popsCols = list(pops.columns)
obCols = list(ob.columns)
len(pops) + len(ob)


wanted_ob = ["t0","u0_amp","tE","log10_thetaE","piE_E","muS_E","mL","piRel","muL_E","muRel_E"]
wanted_pops = ["t0","u0","t_E","theta_E","pi_E","mu_b_S","mass_L","pi_rel","mu_b_L","mu_rel"]
ob_to_pops = {"t0":"t0", "u0_amp":"u0","tE":"t_E","log10_thetaE":"theta_E","piE_E":"pi_E","muS_E":"mu_b_S","mL":"mass_L","piRel":"pi_rel","muL_E":"mu_b_L","muRel_E":"mu_rel"}

def gk(val,d=ob_to_pops):
    keys = [k for k, v in d.items() if v == val]
    if keys:
        return keys[0]
    return None
dfWhole = pd.DataFrame()
for j in wanted_ob:
    for k in range(len(ob[j])):
        dfWhole.at[k,j] = ob[j][k] #0,x 
dict = {"id":[]}
for j in wanted_pops:
    jVal = gk(j)
    dict[jVal] = pops[j]
for i in range(len(pops["rem_id_L"])):
    dict["id"].append(pops["rem_id_L"][i])
dfTotal = pd.concat([dfWhole,pd.DataFrame(dict)])

massGP = [val for val in dfTotal["mL"] if val >= 2.5 and val <= 5]


dfTotal = dfTotal.fillna(1)
dfTotal = pd.concat([dfTotal[[col for col in dfTotal.columns if col != "id"]], dfTotal["id"].replace(101,2)], axis=1)
dfTotal = pd.concat([dfTotal[[col for col in dfTotal.columns if col != "id"]], dfTotal["id"].replace(102,3)], axis=1)
dfTotal = pd.concat([dfTotal[[col for col in dfTotal.columns if col != "id"]], dfTotal["id"].replace(103,4)], axis=1)



xCols = [col for col in dfTotal.columns if col != "id"]
x_data = dfTotal[xCols]
y_data = dfTotal["id"]
X_train, X_t, y_train, y_t = train_test_split(x_data, y_data, test_size = 0.4, random_state=42)
X_test, X_val, y_test, y_val = train_test_split(X_t,y_t,test_size=0.2)



smk = SMOTETomek()
X_res,y_res=smk.fit_resample(X_train, y_train)
smk2 = SMOTETomek()
X_testRes, y_testRes = smk2.fit_resample(X_test,y_test)

y_res = y_res.to_numpy()
y_val = y_val.to_numpy()
y_testRes = y_testRes.to_numpy()
y_res = y_res.astype(int)
y_val = y_val.astype(int)
y_testRes = y_testRes.astype(int)

arr1 = []
for i in range(len(y_res)):
    thing1 = [0,0,0,0,0]
    thing1[y_res[i]]=1
    arr1.append(thing1)        
arr2 = []
for j in range(len(y_val)):
    thing2 = [0,0,0,0,0]
    thing2[y_val[j]]=1
    arr2.append(thing2)
arr3 = []
for k in range(len(y_testRes)):
    thing3 = [0,0,0,0,0]
    thing3[y_testRes[k]]=1 
    arr3.append(thing3)
yTraining = np.array(arr1)
yValidation = np.array(arr2)
yTesting = np.array(arr3)


def getFeatures():
    return X_res, X_val, X_testRes

def getLabels():
    return yTraining, yValidation, yTesting


def getViewData():
    return dfTotal, X_res, y_res