import base64
import io
from io import BytesIO
import re
from tensorflow import keras
#from tensorflow.keras.models import Sequential
#from tensorflow.keras.layers import Dense, Dropout, Flatten
#from tensorflow.keras.layers import Conv2D, MaxPooling2D, Conv3D, BatchNormalization, Activation
#from keras import backend as K
import os
from PIL import Image
import numpy as np
#from sklearn.model_selection import train_test_split
#from sklearn.preprocessing import OneHotEncoder
#import pandas as pd
from tensorflow.keras.models import load_model
#from keras.models import load_model
#model = load_model('model_final.h5')
classes = ['glioma_tumor', 'meningioma_tumor', 'no_tumor', 'pituitary_tumor']

#enc = OneHotEncoder()
#enc.fit([[0], [1], [2], [3]]) 
def names(number):
    if(number == 0):
        return 'a Glioma tumor'
    elif(number == 1):
        return 'a Meningioma tumor'
    elif(number == 2):
        return 'no tumor'
    elif(number == 3):
        return 'a Pituitary tumor'
img_path = "/home/pi/image(2).jpg"
#img_data = base64.b64decode(img_path)  
        
#stream = io.BytesIO(img_data)
img_pil = Image.open(img_path)
        
        
#Load model, change image to array and predict
model = load_model('/home/pi/model_final.h5') 
dim = (150, 150)
        
img = np.array(img_pil.resize(dim))
        
x = img.reshape(1,150,150,3)
answ = model.predict(x)
classification = np.where(answ == np.amax(answ))[1][0]
pred=str(round(answ[0][classification]*100 ,3)) + '% confidence there is ' + names(classification) 
        
        #Second prediction and facts about tumor if there is
if classification==0:
    facts = 'Glioma is a type of tumor that occurs in the brain and spinal cord.\
                    A glioma can affect your brain function and be life-threatening depending on\
                    its location and rate of growth.'
    no_tumor = str(round(answ[0][2]*100 ,3))
    pred2 = no_tumor + '% confidence there is no tumor'
    print(pred)
    print(facts)
    print(pred2)
            
elif classification==1:
    facts = 'A meningioma is a tumor that arises from the meninges, the membranes that surround your brain.\
                    Most meningiomas grow very slowly, often over many years without causing symptoms.'
    no_tumor = str(round(answ[0][2]*100 ,3))
    pred2 = no_tumor + '% confidence there is no tumor'
    print(pred)
    print(facts)
    print(pred2)
        
elif classification==3:
    facts = 'Pituitary tumors are abnormal growths that develop in your pituitary gland.\
                    Most pituitary tumors are noncancerous (benign) growths that remain in your pituitary\
                    gland or surrounding tissues.'
    no_tumor = str(round(answ[0][2]*100 ,3))
    pred2 = no_tumor + '% confidence there is no tumor'
    print(pred)
    print(facts)
    print(pred2)
        
else:
    facts=None
    pred2 = None
