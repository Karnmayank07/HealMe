# -*- coding: utf-8 -*-
"""
Created on Sun May  8 21:01:15 2022

@author: siddhardhan
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu


# loading the saved models

diabetes_model = pickle.load(open('diabetes.sav', 'rb'))

# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('Diabetes prediction Model',
                          
                          ['Diabetes Prediction'],
                          icons=['activity'],
                          default_index=0)
    
    
# Diabetes Prediction Page
if (selected == 'Diabetes Prediction'):
    
    # page title
    st.title('Diabetes Prediction using ML')
    
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
        
    with col2:
        Glucose = st.text_input('Glucose Level (mg/dL)')
    
    with col3:
        BloodPressure = st.text_input('Diastolic Blood Pressure value (mmHg)')
    
    with col1:
        SkinThickness = st.text_input('Skin Thickness value (mm)')
    
    with col2:
        Insulin = st.text_input('Insulin Level (muU/ml)')
    
    with col3:
        BMI = st.text_input('BMI value')
    
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    
    with col2:
        Age = st.text_input('Age of the Person (in Years)')
    
    
    # code for Prediction
    diab_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        if (diab_prediction[0] == 1):
          diab_diagnosis = 'The person may be diabetic'
        else:
          diab_diagnosis = 'The person may not be diabetic'
        
    st.success(diab_diagnosis)


