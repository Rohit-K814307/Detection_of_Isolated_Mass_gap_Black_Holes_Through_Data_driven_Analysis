import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from methods import preProcess_methods
from matplotlib import pyplot as plt
from keras.preprocessing.image import ImageDataGenerator, img_to_array, load_img

getFeatures, getLabels, getViewData = preProcess_methods()

X_res, X_val, X_testRes = getFeatures()
yTraining, yValidation, yTesting = getLabels()


