# -*- coding: utf-8 -*-
"""
Created on Sun december  8 21:01:15 2024

@author: visha
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu # type: ignore


# loading the saved models



heart_disease_model = pickle.load(open('heart_disease_model.sav', 'rb'))

\



# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('Heart Disease Prediction System',
                          
                          ['Heart Disease Prediction'],
                          icons=['heart'],
                          default_index=0)
    
    



# Heart Disease Prediction Page
if (selected == 'Heart Disease Prediction'):
    
    # page title
    st.title('Heart Disease Prediction using ML')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input('Age')
        
    with col2:
        sex = st.text_input('Serum_creatinine')
        
    with col3:
        cp = st.text_input('Ejection_Fraction')
  
        
     
    # code for Prediction
    heart_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Heart Disease Test Result'):
        heart_prediction = loaded_model.predict([[age, Serum_creatinine, Ejection_Fraction ]])                           # type: ignore
        
        if (heart_prediction[0] == 1):
          heart_diagnosis = 'The person is having heart disease'
        else:
          heart_diagnosis = 'The person does not have any heart disease'
        
    st.success(heart_diagnosis)
        
    













