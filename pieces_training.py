# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 16:27:32 2024

@author: t-jan
"""

import tensorflow as tf
import matplotlib.pyplot as plt
from matplotlib.image import imread
import numpy as np

#mnist = tf.keras.datasets.mnist
x_train = []
y_train= []
fen_path = "C:\\Users\\t-jan\\Desktop\\PositionRecognition\\training-data\\boards\\fen.txt"
with open(fen_path, "r") as txt:
    longfen = txt.readlines()
for i in range(1,1281):
    squares_path = "C:\\Users\\t-jan\\Desktop\\PositionRecognition\\training-data\\squares\\" + str(i) + ".jpg"
    x_train.append(imread(squares_path))
    y_train.append(longfen[0][i-1])



#(x_train, y_train), (x_test, y_test) = mnist.load_data()

#x_train = tf.keras.utils.normalize(x_train, axis=1)
#x_test = tf.keras.utils.normalize(x_test, axis=1)


model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Flatten())
model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(13, activation=tf.nn.softmax))

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])
model.fit(x_train, y_train, epochs=3)

#val_loss, val_acc = model.evaluate(x_test, y_test)
#print(val_loss, val_acc)

model.save('pieces.keras')

#new_model = tf.keras.models.load_model('epic_num_reader.model.keras')


#predictions = model.predict([x_test])

'''
j=0
for i in range(0,10000):
    if np.argmax(predictions[i]) != y_test[i]:
        j+=1
        #print("pred: ", np.argmax(predictions[i]))
        #print("true:", y_test[0])
        #plt.imshow(x_test[0], cmap = plt.cm.binary)
#plt.show()
print(j)
'''
