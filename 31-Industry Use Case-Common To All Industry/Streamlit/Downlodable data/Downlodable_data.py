%%writefile Downlodable_data.py

#File name     :  Downlodable_data.py
#Purpose       :  Downlodable data in streamlit using python
#Author        :  Deepsphere.AI, INC.
#Date and Time :  07/07/2021 18:30 hrs

import streamlit as vAR_st 
import streamlit.components as stc
import base64 
import time
timestr = time.strftime("%Y%m%d-%H%M%S")
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
vAR_st.markdown("<h1 style='text-align: center; color: green;'>Download Data in Web Applications Using Streamlit</h1>", unsafe_allow_html=True)

#To customize the background colour of the submit button  
m = vAR_st.markdown("""
<style>
div.stButton > button:first-child {
    background-color: rgb(50,205,50);
}
</style>""", unsafe_allow_html=True)

#To give space between the title and the submit forms
vAR_st.write('')

@vAR_st.cache(suppress_st_warning=True)

# Function for text downloader 
def text_downloader(raw_text):
  b64 = base64.b64encode(raw_text.encode()).decode()
  vAR_filename = "new_text_file_{}_.txt".format(timestr)
  vAR_st.markdown("#### Download File ###")
  href = f'<a href="data:file/txt;base64,{b64}" download="{vAR_filename}">Click Here!!</a>'
  vAR_st.markdown(href,unsafe_allow_html=True)

# Function for csv file downloader 
def csv_downloader(data):
  csvfile = data.to_csv()
  b64 = base64.b64encode(csvfile.encode()).decode()
  vAR_filename = "new_text_file_{}_.csv".format(timestr)
  vAR_st.markdown("#### Download File ###")
  href = f'<a href="data:file/csv;base64,{b64}" download="{vAR_filename}">Click Here!!</a>'
  vAR_st.markdown(href,unsafe_allow_html=True)

col1, col2, col3 = vAR_st.beta_columns([1,3,1])
with col2:
  def main():
    menu = ["Text","CSV","About"]

    vAR_choice = vAR_st.sidebar.selectbox("Menu",menu)

    if vAR_choice == "Text":
      vAR_st.subheader("Text")
      my_text = vAR_st.text_area("Your Message")
      if vAR_st.button("Save"):
        vAR_st.write(my_text)
        text_downloader(my_text)

    elif vAR_choice == "CSV":
      df = pd.read_csv("/content/grades.csv", encoding = 'unicode_escape')
      vAR_st.dataframe(df)
      csv_downloader(df)

    else:
      vAR_st.subheader("About")
      

  if __name__ == '__main__':
    main()

#Disclaimer.

#we are providing this code block strictly for learning and researching, this is not a production 
#ready code. we have no liability on this particular code under any circumstances; user should
#use this code on their own risk. All software, hardware and other products that are refered 
#in these materials belong to the respective vendor who developed or who owns this product.
