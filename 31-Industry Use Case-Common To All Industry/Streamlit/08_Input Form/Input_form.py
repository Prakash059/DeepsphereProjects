%%writefile Input_Form.py

#File name     :  Input_Form.py
#Purpose       :  A simple Input Form for streamlit using python
#Author        :  Deepsphere.AI, INC.
#Date and Time :  24/06/2021 18:30 hrs


import streamlit as vAR_st
import datetime

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
    </style>
    """, unsafe_allow_html=True)

  vAR_st.markdown('<p class="big-font">Master Streamlit With DeepSphere.AI Personalized Learning Platform', unsafe_allow_html=True)

#by this text-align: centre, we can align the title to the centre of the page
vAR_st.markdown("<h1 style='text-align: center; color: green;'>Data Collection: Student Information</h1>", unsafe_allow_html=True)

#To customize the background colour of the submit button  
m = vAR_st.markdown("""
<style>
div.stButton > button:first-child {
    background-color: rgb(50,205,50);
}
</style>""", unsafe_allow_html=True)

col2, colA, colB, col1 = vAR_st.beta_columns((1,1,1,1))
with colA:
#with vAR_st.text_input() we can take the user input
  vAR_first_name  = vAR_st.text_input('First Name')
  vAR_start_date  = datetime.date(1995, 7, 6)
  vAR_date        = vAR_st.date_input('Date of Birth',vAR_start_date)
  vAR_email       = vAR_st.text_input('Email')
with colB:
  vAR_last_name   = vAR_st.text_input("Last Name")
  vAR_grade       = vAR_st.text_input('Grade')
  vAR_phone       = vAR_st.text_input('Phone number')   

#for user input
col_space1, col_address, col_space2 = vAR_st.beta_columns((1,2,1))
with  col_address:
# if we need to input more characters, we can use vAR_st.text_area()
  vAR_address     = vAR_st.text_area('Address')


col_space, col_submit, col_space3 = vAR_st.beta_columns((5,1,5))
with col_submit:
#for the submit button use vAR_st.button()
  vAR_submit_button = vAR_st.button('submit')  


#to display the user input after hiting the submit button
if vAR_submit_button: 

  col_2, col_A, col_B, col_1 = vAR_st.beta_columns((1,1,1,1))
  with col_A:
    vAR_st.subheader('First Name')
    vAR_st.info(vAR_first_name)
    vAR_st.subheader('Date of Birth')
    vAR_st.info(vAR_date)
    vAR_st.subheader('Email')
    vAR_st.info(vAR_email)
  with col_B:
    vAR_st.subheader('Last Name')
    vAR_st.info(vAR_last_name)
    vAR_st.subheader('Grade')
    vAR_st.info(vAR_grade)
    vAR_st.subheader('Phone Number')
    vAR_st.info(vAR_phone)
 
#to display the user input after hiting the submit button
  col_space_1, col_address1, col_space_2 = vAR_st.beta_columns((1,2,1))   
  with col_address1:
    vAR_st.subheader('Address')
    vAR_st.info(vAR_address)



#Disclaimer.

#we are providing this code block strictly for learning and researching, this is not a production 
#ready code. we have no liability on this particular code under any circumstances; user should
#use this code on their own risk. All software, hardware and other products that are refered 
#in these materials belong to the respective vendor who developed or who owns this product.


