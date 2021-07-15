%%writefile app.py

#File name     :  app.py
#Purpose       :  Simple Mandatory Form Validation
#Author        :  Deepsphere.AI
#Date and Time :  2/07/2021 18:30 hrs


import streamlit as vAR_st
import re

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
vAR_st.markdown("<h1 style='text-align: center; color: green;'>Streamlit Simplifies Mandatory Form Validation for Data Science</h1>", unsafe_allow_html=True)

#To customize the background colour of the submit button  
m = vAR_st.markdown("""
<style>
div.stButton > button:first-child {
    background-color: rgb(50,205,50);
}
</style>""", unsafe_allow_html=True)

#To give space between the title and the user input
vAR_st.write('')

col2, colA, colB, col1 = vAR_st.beta_columns((1,1,1,1))
with colA:
  #For the user input can use vAR_st.text_input()
  vAR_first_name  = vAR_st.text_input('First Name in UPPER CAPS:')
  vAR_age         = vAR_st.text_input('Age')
  vAR_pincode     = vAR_st.text_input('Pincode')
  vAR_state       = vAR_st.text_input('State')
  vAR_st.write('')
  vAR_terms       = vAR_st.checkbox('I have read and agree to the terms')
  
with colB:
  vAR_last_name   = vAR_st.text_input('Last Name in UPPER CAPS:')
  vAR_email       = vAR_st.text_input('Email')
  vAR_address     = vAR_st.text_area('Address')


col_space, col_submit, col_space3 = vAR_st.beta_columns((5,1,5))
with col_submit:
  #for the submit button use vAR_st.button()
  vAR_submit_button = vAR_st.button('submit')  


with col1:
  if vAR_submit_button:

  #if there is any error in vAR_first_name
    if len(vAR_first_name) > 0:
      if vAR_first_name.strip().isalpha(): 

        #isupper() functions helps us to check whether the input given is in upper caps or not 
        if not vAR_first_name.isupper():
          vAR_st.error('Enter First Name in UPPER CAPS')
      
      else:
        vAR_st.error('Name must be a String')  

    #if we submit the form without giving information of first name, an error appears
    else:
      vAR_st.error('First Name is Required')


  #if there is any error in vAR_last_name
    if len(vAR_last_name) > 0:
      if vAR_last_name.strip().isalpha(): 

        #isupper() functions helps us to check whether the input given is in upper caps or not 
        if not vAR_last_name.isupper():
          vAR_st.error('Enter Last Name in UPPER CAPS')

      else:
        vAR_st.error('Name must be a String') 

    #if we submit the form without giving information of last name, an error appears
    else:
      vAR_st.error('Last Name is Required')


  #if there is any error in vAR_age
    if len(vAR_age) > 0:
      if vAR_age.strip().isdigit(): 
        
        #if age is below 18, an error message pops 
        if int (vAR_age) < 18:
          vAR_st.error('Age Restriction')  

      else:
        vAR_st.error('Age must be integer')

    #if we submit the form without giving information of age, an error appears      
    else:
      vAR_st.error('Age is Required')


  #if there is any error in vAR_email
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if len(vAR_email) > 0:
      if not (re.match(regex, vAR_email)):
        vAR_st.error("Invalid Email")
    
    #if we submit the form without giving information of email, an error appears
    else:
      vAR_st.error('Email is Required')


  #if there is any error in vAR_address
    if len(vAR_address) > 0:

      #if the address bar exceeds more than 45 characters it shows an error 
      if len(vAR_address) > 45:
        vAR_st.error('You Entered More than the Acceptable Field Length')
    
    #if we submit the form without giving information of adress, an error appears
    else:
      vAR_st.error('Adress is Required')


  #if there is any error in vAR_pincode
    if len(vAR_pincode) > 0:
      if len(vAR_pincode) != 6:
        vAR_st.error('Invalid Pincode')
    
    #if we submit the form without giving information of pincode, an error appears
    else:
      vAR_st.error('Pincode is Required')


    #if we submit the form without giving information of state, an error appears
    if len(vAR_state) == 0:
      vAR_st.error('State is Required')

    #if we submit the form without accepting to the terms, an error eppers
    if not vAR_terms:
      vAR_st.error('Accept to the terms')
    


#Disclaimer.

#we are providing this code block strictly for learning and researching, this is not a production 
#ready code. we have no liability on this particular code under any circumstances; user should
#use this code on their own risk. All software, hardware and other products that are refered 
#in these materials belong to the respective vendor who developed or who owns this product.            

