import tensorflow as tf
from tensorflow import keras
from keras.callbacks import EarlyStopping
import numpy as np
from methods import preProcess_methods
getFeatures, getLabels, getViewData = preProcess_methods()

def model(metrics):
   
    inputs = keras.Input(shape=(10,))
    net = tf.keras.layers.Dense(32, activation='relu')(inputs)
    net = tf.keras.layers.Dropout(0.2)(net)
    net = tf.keras.layers.Dense(64, activation='relu')(net)
    out = tf.keras.layers.Dense(5, activation='softmax')(net)
    
    model = tf.keras.models.Model(inputs=inputs, outputs=out)
    model.compile(tf.keras.optimizers.Adam(learning_rate=1e-5), loss='categorical_crossentropy', metrics=metrics)
    
    return model

es = EarlyStopping(monitor='val_loss', mode='min', verbose=1, patience=10)

METRICS = [
    tf.keras.metrics.BinaryAccuracy(name='accuracy'),
      tf.keras.metrics.Precision(name='precision'),
      tf.keras.metrics.Recall(name='recall')
]

massDet = model(METRICS)

X_res, X_val, X_testRes = getFeatures()
yTraining, yValidation, yTesting = getLabels()
train_history = massDet.fit(X_res, yTraining, validation_data=(X_val, yValidation), epochs=4000, verbose=2, callbacks=[es])

def getTrain_history():
    return train_history

massDet.save_weights('save_model/model')
