# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 07:22:22 2024

@author: rajad
"""

import numpy as np
import pickle 
import streamlit as st

#loading the Saved Model
loaded_model = pickle.load(open('D:/Project/Model/trained_model.sav', 'rb'))

#creating a function 
def heart_prediction(input_data):
    
    input_data_as_numpy_array= np.asarray(input_data)

    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0]== 0):
      return 'The Person does not have a Heart Disease'
    else:
      return 'The Person has Heart Disease'
  
def main():

        st.title('Heart Disease Prediction Web App')
        
        serum_creatinine = st.text_input('Serum Creatinine') 
        ejection_fraction = st.text_input('Ejection Fraction') 
        age = st.text_input('age') 
        
        #code for prediction 
        diagnosis = ''
        
        #creating a button for prediction 
        if st.button('Heart Disease Test Result'):
          diagnosis = heart_prediction([serum_creatinine, ejection_fraction, age])
          
        st.success(diagnosis)


if __name__ == '__main__':
    main()
    
        