%%writefile Data_Filtering.py

#File name     :  Data_Filtering.py
#Purpose       :  Data Filtering on Streamlit using python
#Author        :  Deepsphere.AI, INC.
#Date and Time :  07/07/2021 18:30 hrs

import streamlit as vAR_st 
import pandas as pd 

#for Setting the page layout to wide
vAR_st.set_page_config(layout="wide")

#for having the logo and title in the same line we use vAR.st_beta_columns() and make the ratio accordingly 
vAR_logo, vAR_title = vAR_st.beta_columns((6,50))
with vAR_logo:
  vAR_st.image('https://raw.githubusercontent.com/DeepsphereAI/IndustryUseCases/main/31-Industry%20Use%20Case-Common%20To%20All%20Industry/Streamlit/Logo/logo.jpg')
with vAR_title:
#setting font size and colour for the title 
  vAR_st.markdown("""
  <style>
  .big-font {
    font-size:30px !important;
  }
  </style>""", unsafe_allow_html=True)

  vAR_st.markdown('<p class="big-font">Master Streamlit With DeepSphere.AI Personalized Learning Platform', unsafe_allow_html=True)

#by this text-align: centre, we can align the title to the centre of the page
vAR_st.markdown("<h1 style='text-align: center; color: green;'>Data Filtering using Streamlit</h1>", unsafe_allow_html=True)

vAR_st.write('')

col1, col2, col3 = vAR_st.beta_columns([1,3,1])
with col2:
  df = pd.read_csv("/content/grades.csv")
  cols = ["Last name", "First name", "SSN", "Test1", " Test2", "Test3" , "Test4", "Final", "Grade"]
  vAR_options = vAR_st.multiselect("Columns", df.columns.tolist(), default=cols)
  vAR_st.dataframe(df[vAR_options])


#Disclaimer.

#we are providing this code block strictly for learning and researching, this is not a production 
#ready code. we have no liability on this particular code under any circumstances; user should
#use this code on their own risk. All software, hardware and other products that are refered 
#in these materials belong to the respective vendor who developed or who owns this product.
