import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from methods import preProcess_methods
from matplotlib import pyplot as plt
from sklearn.metrics import plot_confusion_matrix
from model import getTrain_history

getFeatures, getLabels, getViewData = preProcess_methods()

X_res, X_val, X_testRes = getFeatures()
yTraining, yValidation, yTesting = getLabels()

METRICS = [
    tf.keras.metrics.BinaryAccuracy(name='accuracy'),
      tf.keras.metrics.Precision(name='precision'),
      tf.keras.metrics.Recall(name='recall')
]

def model(metrics):
   
    inputs = keras.Input(shape=(10,))
    net = tf.keras.layers.Dense(32, activation='relu')(inputs)
    net = tf.keras.layers.Dropout(0.2)(net)
    net = tf.keras.layers.Dense(64, activation='relu')(net)
    out = tf.keras.layers.Dense(5, activation='softmax')(net)
    
    model = tf.keras.models.Model(inputs=inputs, outputs=out)
    model.compile(tf.keras.optimizers.Adam(learning_rate=1e-5), loss='categorical_crossentropy', metrics=metrics)
    
    return model

modl = model(METRICS)
modl.load_weights("save_model/model")

train_history = getTrain_history()
acc = train_history.history['accuracy']
val_acc = train_history.history['val_accuracy']
loss = train_history.history['loss']
val_loss = train_history.history['val_loss']

epochs = range(1, len(acc) + 1)
plt.figure(figsize=(8, 6), dpi=100)
plt.plot(epochs, acc, 'bo', label='Training acc')
plt.plot(epochs, val_acc, 'b', label='Validation acc')
plt.title('Training and validation accuracy')
plt.legend()

plt.figure(figsize=(8, 6), dpi=100)

plt.plot(epochs, loss, 'bo', label='Training loss')
plt.plot(epochs, val_loss, 'b', label='Validation loss')
plt.title('Training and validation loss')
plt.legend()

plt.show()



t_pred = modl.predict(X_testRes)
t_true = yTesting

class estimator:
  _estimator_type = ''
  classes_=[]
  def __init__(self, model, classes):
    self.model = model
    self._estimator_type = 'classifier'
    self.classes_ = classes
  def predict(self, X):
    y_prob= self.model.predict(X)
    y_pred = y_prob.argmax(axis=1)
    return y_pred

classifier = estimator(modl, [0,1,2,3,4])

disp = plot_confusion_matrix(classifier, X=X_testRes, y_true=np.argmax(yTesting,axis=1),cmap=plt.cm.Blues)
plt.title('Confusion matrix')
fig = disp.figure_
fig.set_figwidth(15)
fig.set_figheight(15) 
plt.show()