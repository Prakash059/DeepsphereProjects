%%writefile Maps.py

#File name     :  Maps.py
#Purpose       :  Visualize Maps Using Streamlit
#Author        :  Deepsphere.AI, INC.
#Date and Time :  07/07/2021 18:30 hrs


import streamlit as vAR_st
import pandas as pd
import numpy as np


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
vAR_st.markdown("<h1 style='text-align: center; color: green;'>Visualize Maps Using Streamlit</h1>", unsafe_allow_html=True)

col1, col2, col3 = vAR_st.beta_columns([1,3,1])
with col2:
  data = pd.read_csv('/content/world_country_and_usa_states_latitude_and_longitude_values.csv')

  df_2 = pd.DataFrame(data[:200],columns = ['latitude','longitude','country'])
  df = pd.DataFrame(data[:200],columns = ['latitude','longitude'])
  vAR_st.write(df_2)
  vAR_st.map(df)

  vAR_st.write('')
  vAR_st.write('')
  
  df_1 = pd.DataFrame(
     np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
     columns=['lat', 'lon'])

  vAR_st.map(df_1)

  
#Disclaimer.

#we are providing this code block strictly for learning and researching, this is not a production 
#ready code. we have no liability on this particular code under any circumstances; user should
#use this code on their own risk. All software, hardware and other products that are refered 
#in these materials belong to the respective vendor who developed or who owns this product.
