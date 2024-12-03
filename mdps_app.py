# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 01:02:08 2024

@author: visha
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

#loading the saved models

loaded_model = pickle.load(open('C:/Users/visha/Desktop/ML project/trained_model.sav', 'rb'))

with st.sidebar:
    
    selected = option_menu('Heart Disease Prediction System',
                           
                           ['Predictor'],
                          
                          icons=['heart'],
                          default_index=0)
    
    if (selected == ' Predictor'):
        st.title('Heart Disease Prediction using ML')

    col1, col2, col3 = st.columns(2) 
    with col1:
       serum_creatinine = st.text_input('Serum Creatinine') 
    with col2:
       serum_creatinine = st.text_input('Ejection Fraction')
    with col3:
       age = st.text_input('Age')
       
       #code for prediction
       
    diagnosis = ''
          
          #creating a button for prediction 
    if st.button('Heart Disease Test Result'):
            diagnosis = loaded_model.predict([serum_creatinine, ejection_fraction, age])
        
            if (diagnosis[0]== 0): 
    return 'The Person does not have a Heart Disease'
        else:
          return 'The Person has Heart Disease'
        
    st.success(diagnosis)
