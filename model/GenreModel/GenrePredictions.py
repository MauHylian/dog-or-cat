#!/usr/bin/env python

import cv2
import tensorflow as tf

CATEGORIES = ["Cumbion", "Rock"]

def prepare(filepath):
    IMG_SIZEa = 1000
    IMG_SIZEb = 400
    img_array = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
    img_array = img_array/255.0
    new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
    return new_array.reshape(-1, IMG_SIZEa, IMG_SIZEb, 1)


model = tf.keras.models.load_model("ejemplocnn.model")

prediction = model.predict([prepare('gatin.jpg')])
print(prediction)  # will be a list in a list.
print(CATEGORIES[int(prediction[0][0])])

