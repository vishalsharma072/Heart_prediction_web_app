# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 00:07:41 2024

@author: visha
"""
import numpy as np
import pickle 

#loading the saved model
loaded_model = pickle.load(open('trained_model.sav', 'rb'))

input_data = (1.3,25,65)

input_data_as_numpy_array= np.asarray(input_data)

input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

prediction = loaded_model.predict(input_data_reshaped)
print(prediction)

if (prediction[0]== 0):
  print('The Person does not have a Heart Disease')
else:
  print('The Person has Heart Disease')
