%%writefile Streamlit_checkbox.py

#File name     :  Streamlit_checkbox
#Purpose       :  A simple Checkbox for streamlit using python
#Author        :  Deepsphere.AI, INC.
#Date and Time :  24/06/2021 18:30 hrs


import streamlit as vAR_st

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
  .big-font {font-size:30px !important;
  }
  </style>""", unsafe_allow_html=True)

  vAR_st.markdown('<p class="big-font">Master Streamlit With DeepSphere.AI Personalized Learning Platform', unsafe_allow_html=True)

#by this text-align: centre, we can align the title to the centre of the page
vAR_st.markdown("<h1 style='text-align: center; color: green;'>A Simple Check Box</h1>", unsafe_allow_html=True)

#To customize the background colour of the submit button  
m = vAR_st.markdown("""
<style>
div.stButton > button:first-child {
    background-color: rgb(50,205,50);
}
</style>""", unsafe_allow_html=True)

col2, colA, col1 = vAR_st.beta_columns((1,1,1))
with colA:
#we will be using vAR_st.checkbox() for creating checkbox
    x = vAR_st.checkbox('Andhra')
    y = vAR_st.checkbox('Telangana')
    z = vAR_st.checkbox('Tamilnadu')


col_space, col_submit, col_space1 = vAR_st.beta_columns((5,1,5))
with col_submit:
#for the submit button use vAR_st.button()
  vAR_submit_button = vAR_st.button('submit')  

  

col_space, col_submit, col_space1 = vAR_st.beta_columns((1,1,1))
with col_submit:
#to display the user input, if we hit the submit button your selected options will appear 
  if vAR_submit_button:
    vAR_st.write('You selected:')
    if x:
      vAR_st.info('Andhra')
    if y:
      vAR_st.info('Telangana')
    if z:
      vAR_st.info('Tamilnadu') 




#Disclaimer.

#we are providing this code block strictly for learning and researching, this is not a production 
#ready code. we have no liability on this particular code under any circumstances; user should
#use this code on their own risk. All software, hardware and other products that are refered 
#in these materials belong to the respective vendor who developed or who owns this product.