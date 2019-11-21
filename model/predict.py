#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import cv2
import tensorflow as tf
import os
import sys

import config

CATEGORIES = config.CATEGORIES

model = tf.keras.models.load_model(config.MODEL)

def prepare(filepath):
    IMG_SIZE = 50  # 50 in txt-based
    img_array = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
    img_array = img_array/255.0
    new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
    return new_array.reshape(-1, IMG_SIZE, IMG_SIZE, 1)

def predict(path):
    try:
        prediction = model.predict([prepare(os.path.abspath(path))])
        prediction = prediction[0][0]
        return CATEGORIES[int(round(prediction))]
    except Exception as e:
        print(e)
        return None


# In[ ]:




