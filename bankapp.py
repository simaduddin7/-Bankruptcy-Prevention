# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 11:52:14 2023

@author: pranay
"""


import numpy as np
import pickle
import pandas as pd
import streamlit as st
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from PIL import Image

pickle_in = open("svm2.pkl","rb")
classifier=pickle.load(pickle_in)

def welcome():
    return "Welcome ALL"
def predict_bankruptcy(industrial_risk, management_risk, financial_flexibility, credibility, competitiveness, operating_risk):
     industrial_risk = float(industrial_risk)
     management_risk = float(management_risk)
     financial_flexibility = float(financial_flexibility)
     credibility = float(credibility)
     competitiveness = float(competitiveness)
     operating_risk = float(operating_risk)    
     input_data = np.array([[industrial_risk, management_risk, financial_flexibility, credibility, competitiveness, operating_risk]])
     prediction=classifier.predict(input_data)
     print(prediction)
     return prediction





def main():
    st.title("Bankruptcy Detector")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Bankruptcy Detector ML App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    industrial_risk = st.text_input("industrial_risk","Type Here")
    management_risk = st.text_input(" management_risk","Type Here")
    financial_flexibility = st.text_input(" financial_flexibility","Type Here")
    credibility = st.text_input(" credibility","Type Here")
    competitiveness = st.text_input(" competitiveness","Type Here")
    operating_risk = st.text_input(" operating_risk","Type Here")
    result=""
    if st.button("Predict"):
        result=predict_bankruptcy(industrial_risk, management_risk, financial_flexibility, credibility, competitiveness, operating_risk)
        output_message = "No bankruptcy" if result == 1 else "Bankruptcy"
    
    st.success(f'There will be {output_message}')
   #st.success('The output is {}'.format(result))
    if st.button("About"):
        st.text("Lets LEarn")
        st.text("Built with Streamlit")

if __name__=='__main__':
    main()