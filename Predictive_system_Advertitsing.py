# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import pickle

#loading saved model 
loaded_algo =pickle.load (open('D:/TAPIWA_WORK/Models/advertisement_trained_algo.sav','rb'))

input_data  = (47.64,49,45632.51,122.02,0)
# 47.64,49,45632.51,122.02,0

#changing data set into a numpy array 
input_data_asarray = np.asanyarray(input_data)

#changing shape of array 
input_data_reshaped= input_data_asarray.reshape(1,-1)

#making prediction
prediction =loaded_algo.predict(input_data_reshaped)

print(prediction)

if (prediction[0] ==1):
    print('This person will most likely click on the advert')
else:
    print ('This person will not click on the advert')




   