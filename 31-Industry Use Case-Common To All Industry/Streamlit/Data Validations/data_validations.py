%%writefile app.py

#File name     :  app.py
#Purpose       :  Simple Data & Field Validations
#Author        :  Deepsphere.AI
#Date and Time :  2/07/2021 18:30 hrs


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
  .big-font {
    font-size:30px !important;
  }
  </style>""", unsafe_allow_html=True)

  vAR_st.markdown('<p class="big-font">Master Streamlit With DeepSphere.AI Personalized Learning Platform', unsafe_allow_html=True)

#by this text-align: centre, we can align the title to the centre of the page
vAR_st.markdown("<h1 style='text-align: center; color: green;'>Streamlit Simplifies Data Validation for Data Science</h1>", unsafe_allow_html=True)

#To customize the background colour of the submit button  
m = vAR_st.markdown("""
<style>
div.stButton > button:first-child {
    background-color: rgb(50,205,50);
}
</style>""", unsafe_allow_html=True)

#To give space between the title and the submit forms
vAR_st.write('')

col1, col2, col3, col4, col5= vAR_st.beta_columns((1,5,1,5,1))
with col2:
  #creating a form for user to input an inter number and every form must contain a submit button 
  with vAR_st.form(key='my_form'):
    vAR_number        = vAR_st.text_input('Enter an Integer: Data Validation Performed on Submit')
    vAR_submit_button = vAR_st.form_submit_button(label='Submit')

    if len(vAR_number) > 0:

      #isdigit() function is used to check whether the entered number is integer or not
      if vAR_number.strip().isdigit(): 

        #if there are any field length Validations we can restrict them by if condition 
        if len(vAR_number) < 6:
          vAR_st.success('You Entered an Integer')
        else:
            vAR_st.warning('You Entered More than the Acceptable Field Length')
      
      else:
        vAR_st.warning('You Should Enter an Integer')

with col4:
  #creating a form for user to input a string 
  with vAR_st.form(key='my_Form'):
    vAR_string    = vAR_st.text_input('Enter a String: Data Validation Performed on Submit')
    vAR_submit_button = vAR_st.form_submit_button(label='Submit')

    if len(vAR_string) > 0:

      #isalpha() function is used to check whether the entered input is string or not
      if vAR_string.strip().isalpha(): 

        #if there are any field length Validations we can restrict them by if condition 
        if len(vAR_string) < 6:
          vAR_st.success('You Entered a String')
        else:
            vAR_st.warning('You Entered More than the Acceptable Field Length')
      
      else:
        vAR_st.warning('You Should Enter a String') 

vAR_st.write('')
vAR_st.write('')

col1, col2, col3, col4, col5= vAR_st.beta_columns((1,5,1,5,1))
with col2:

  #creating a form for user to input date in given format
  with vAR_st.form(key='My_form'):
    vAR_date      = vAR_st.text_input("Enter Date in MM-DD-YYYY Format: Data Validation Performed on Submit")
    vAR_submit_button = vAR_st.form_submit_button(label='Submit')

    if len(vAR_date) > 0:

      #split(-) function will seperate the month, day, year we entered 
      #and with map() function it matches with vAR_month, vAR_day and vAR_year
      vAR_month, vAR_day, vAR_year = map(int, vAR_date.split('-'))
      if (vAR_month > 12 or vAR_day >31 or vAR_month < 1 or vAR_day < 1 ):
        vAR_st.warning('You Entered Wrong Format')
      else:
        vAR_st.success('You Entered a Valid Date')  

with col4:
  with vAR_st.form(key='My_Form'):
    #creating a form for user to input a float number
    vAR_float     = vAR_st.text_input('Enter a Float: Data Validation Performed on Submit')
    vAR_submit_button = vAR_st.form_submit_button(label='Submit')

    if len(vAR_float) > 0:

      #if there are any field length Validations we can restrict them by if condition 
      if len(vAR_float) < 6:

        #isdigit() function is used to check whether the entered number is integer or not. 
        #So if its a integer, we'll get a warning sign
        if vAR_float.strip().isdigit():
          vAR_st.warning('You Should Enter a Float Number')
          vAR_st.stop()

        #here replace() function is used to replace the '.' with '' 
        #so that after using replace function we could get an integer, 
        #so if the output is integer the the entered input is float number
        if vAR_float.replace('.', '', 1).isdigit():
          vAR_st.success('You Entered a Valid Float Digit')
        else:
          vAR_st.warning('You Should Enter a Float Number')
      
      else:
        vAR_st.warning('You Entered More than the Acceptable Field Length')
 

 
#Disclaimer.

#we are providing this code block strictly for learning and researching, this is not a production 
#ready code. we have no liability on this particular code under any circumstances; user should
#use this code on their own risk. All software, hardware and other products that are refered 
#in these materials belong to the respective vendor who developed or who owns this product.             