%%writefile Data_Visualization.py

#File name     :  Data_Visualization.py
#Purpose       :  Data Visualization Using Streamlit
#Author        :  Deepsphere.AI, INC.
#Date and Time :  07/07/2021 18:30 hrs


import streamlit as vAR_st
import pandas as pd
import numpy as np
import plotly.figure_factory as ff
import matplotlib.pyplot as plt



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
vAR_st.markdown("<h1 style='text-align: center; color: green;'>Data Visualization Using Streamlit</h1>", unsafe_allow_html=True)


col1, col2, col3 = vAR_st.beta_columns([1,3,1])
with col2:
  @vAR_st.cache
  def load_data(nrows):
    data = pd.read_csv('/content/1000_Sales_Records.csv', nrows=nrows)
    return data

  @vAR_st.cache
  def load_center_data(nrows):
    data = pd.read_csv('/content/electronic-card-transactions-may-2021-csv-tables.csv',nrows=nrows)
    return data

  @vAR_st.cache
  def load_meal_data(nrows):
    data = pd.read_csv('/content/annual-enterprise-survey-2020-financial-year-provisional-csv.csv',nrows=nrows)
    return data


  Sales_Records = load_data(50)
  transactions = load_center_data(50)
  annual_enterprise = load_meal_data(50)


#Sales_Records
  vAR_st.subheader('Sales_Records')
  vAR_st.write(Sales_Records)

  vAR_st.bar_chart(Sales_Records['Units Sold'])
  df = pd.DataFrame(Sales_Records[:20], columns = ['Total Revenue','Total Cost','Total Profit'])
  df.hist()


  vAR_st.line_chart(df)

  chart_data = pd.DataFrame(Sales_Records[:40], columns=['Unit Price', 'Unit Cost'])
  vAR_st.area_chart(chart_data)

#Transactions
  vAR_st.subheader('Transactions')
  if vAR_st.checkbox('Show Transactions data'):
    vAR_st.subheader('Transactions data')
    vAR_st.write(transactions)

  vAR_st.bar_chart(transactions['Data_value'])


  vAR_st.subheader('Annual_Enterprise')
  vAR_st.bar_chart(annual_enterprise['Value'])
  agree = vAR_st.button('Click to see Annual_Enterprise')
  if agree:
    vAR_st.write(annual_enterprise)



  
#Disclaimer.

#we are providing this code block strictly for learning and researching, this is not a production 
#ready code. we have no liability on this particular code under any circumstances; user should
#use this code on their own risk. All software, hardware and other products that are refered 
#in these materials belong to the respective vendor who developed or who owns this product.
