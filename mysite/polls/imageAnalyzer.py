import tensorflow as tf
from keras import models, layers
from keras.applications import VGG16
from keras.applications.vgg16 import decode_predictions
import numpy as np
from PIL import Image
import sys
import os

model = VGG16(weights = 'imagenet')
image_w = 224
image_h = 224
result = np.empty(20, object)

def imagePredict(image) :
    image = '.' + image
    
    img = Image.open(image)
    img = img.resize((image_w, image_h))

    x = np.asarray(img)
    x = np.expand_dims(x,0)

    yhat = model.predict(x)
    label = decode_predictions(yhat, top=20)
    for i in range(0, 20) :
        result[i] = str(i+1) + ". 예측 결과 : " + str(label[0][i][2]*100) + "% 확률로 "+ label[0][i][1] + "입니다." 
    print(label)
    print(result)
    return result
    
