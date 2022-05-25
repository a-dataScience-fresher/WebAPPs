# -*- coding: utf-8 -*-
"""
Created on Mon May 23 09:40:07 2022

@author: Tapiwanashe
"""

import numpy as np
import pickle
import streamlit as st


#loading the saved model
loaded_algo =pickle.load (open('D:/TAPIWA_WORK/Models/advertisement_trained_algo2.sav','rb'))

#creating a function for prediction 

def advert_click_pred(input_data):
    
    #input_data  = (47.64,49,45632.51,122.02,0)

    #changing data set into a numpy array 
    input_data_asnumpyarray = np.asarray(input_data)

    #changing shape of array 
    input_data_reshaped= input_data_asnumpyarray.reshape(1,-1)

    #making prediction
    prediction =loaded_algo.predict(input_data_reshaped)
    
    

    print(prediction)

    if (prediction[0] ==0):
        return 'This person will not click on the advert'
    else:
        return 'This person will most likely click on the advert'



def main():
    st.title('Is a client likely to click on the advert or NO?')
    Time= st.text_input('Time spent on site in minutes')
    Age = st.text_input('Age of the client')
    AvgIncome= st.text_input('Average area income of geographic area')
    Daily = st.text_input('Time spent on internet in minutes')
    sex=st.text_input('Male =1 and Female = 0')
    
    
    #code for outcome 
    outcome =''
    
    #creating abutton 
    if st.button ('AD click results'):
        outcome = advert_click_pred([Time,Age,AvgIncome,Daily,sex])
    st.success(outcome)
    



if __name__ == '__main__':
    main() 
    