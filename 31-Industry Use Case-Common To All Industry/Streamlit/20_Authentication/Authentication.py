%%writefile Authentication.py

#File name     :  Authentication.py
#Purpose       :  Authenticating  Using Streamlit
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
vAR_st.markdown("<h1 style='text-align: center; color: green;'>Authenticating  Using Streamlit</h1>", unsafe_allow_html=True)

#To customize the background colour of the submit button  
m = vAR_st.markdown("""
<style>
div.stButton > button:first-child {
    background-color: rgb(50,205,50);
}
</style>""", unsafe_allow_html=True)

#To give space between the title and the submit forms
vAR_st.write('')

col1, col2, col3 = vAR_st.beta_columns([1,2,1])
with col2:
# Security
#passlib,hashlib,bcrypt,scrypt
  import hashlib
  def make_hashes(password):
    return hashlib.sha256(str.encode(password)).hexdigest()

  def check_hashes(password,hashed_text):
    if make_hashes(password) == hashed_text:
      return hashed_text
    return False
# DB Management
  import sqlite3 
  conn = sqlite3.connect('data.db')
  c = conn.cursor()
# DB  Functions
  def create_usertable():
    c.execute('CREATE TABLE IF NOT EXISTS userstable(username TEXT,password TEXT)')


  def add_userdata(username,password):
    c.execute('INSERT INTO userstable(username,password) VALUES (?,?)',(username,password))
    conn.commit()

  def login_user(username,password):
    c.execute('SELECT * FROM userstable WHERE username =? AND password = ?',(username,password))
    data = c.fetchall()
    return data


  def view_all_users():
    c.execute('SELECT * FROM userstable')
    data = c.fetchall()
    return data


  def main():
    """Simple Login App"""

    vAR_st.title("Simple Login App")

    menu = ["Home","Login","SignUp"]
    choice = vAR_st.sidebar.selectbox("Menu",menu)

    if choice == "Home":
      vAR_st.subheader("Home")

    elif choice == "Login":
      vAR_st.subheader("Login Section")

      username = vAR_st.sidebar.text_input("User Name")
      password = vAR_st.sidebar.text_input("Password",type='password')
      if vAR_st.sidebar.checkbox("Login"):
      # if password == '12345':
        create_usertable()
        hashed_pswd = make_hashes(password)

        result = login_user(username,check_hashes(password,hashed_pswd))
        if result:

          vAR_st.success("Logged In as {}".format(username))

          task = vAR_st.selectbox("Task",["Add Post","Analytics","Profiles"])
          if task == "Add Post":
            vAR_st.subheader("Add Your Post")

          elif task == "Analytics":
            vAR_st.subheader("Analytics")
          elif task == "Profiles":
            vAR_st.subheader("User Profiles")
            user_result = view_all_users()
            clean_db = pd.DataFrame(user_result,columns=["Username","Password"])
            vAR_st.dataframe(clean_db)
        else:
          vAR_st.warning("Incorrect Username/Password")

    elif choice == "SignUp":
      vAR_st.subheader("Create New Account")
      new_user = vAR_st.text_input("Username")
      new_password = vAR_st.text_input("Password",type='password')

      if vAR_st.button("Signup"):
        create_usertable()
        add_userdata(new_user,make_hashes(new_password))
        vAR_st.success("You have successfully created a valid Account")
        vAR_st.info("Go to Login Menu to login")


  if __name__ == '__main__':
    main()
#Disclaimer.

#we are providing this code block strictly for learning and researching, this is not a production 
#ready code. we have no liability on this particular code under any circumstances; user should
#use this code on their own risk. All software, hardware and other products that are refered 
#in these materials belong to the respective vendor who developed or who owns this product.
