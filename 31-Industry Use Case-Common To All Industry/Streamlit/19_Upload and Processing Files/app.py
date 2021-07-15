%%writefile app.py

#File name     :  app.py
#Purpose       :  Upload and Process Files Using Streamlit
#Author        :  Deepsphere.AI, INC.
#Date and Time :  07/07/2021 18:30 hrs



#along with !pip install streamlit and !pip install pyngrok
#we need pip install docx2txt , pip install PyPDF3 , pip install pdfplumber

import streamlit as vAR_st
import streamlit.components.v1 as stc
# File Processing Pkgs
import pandas as pd
import docx2txt
from PIL import Image 
from PyPDF3 import PdfFileReader
import pdfplumber


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
vAR_st.markdown("<h1 style='text-align: center; color: green;'>Upload and Process Files Using Streamlit</h1>", unsafe_allow_html=True)


def read_pdf(file):
  pdfReader = PdfFileReader(file)
  count = pdfReader.numPages
  all_page_text = ""
  for i in range(count):
    page = pdfReader.getPage(i)
    all_page_text += page.extractText()

  return all_page_text

def read_pdf_with_pdfplumber(file):
  with pdfplumber.open(file) as pdf:
      page = pdf.pages[0]
      return page.extract_text()


# Fxn
@vAR_st.cache
def load_image(image_file):
  img = Image.open(image_file)
  return img 

col1, col2, col3 = vAR_st.beta_columns([1,3,1])
with col2:
  def main():

    menu = ["Images","Dataset","DocumentFiles","About"]
    choice = vAR_st.sidebar.selectbox("Menu",menu)

    if choice == "Images":
      vAR_st.subheader("Images")
      image_file = vAR_st.file_uploader("Upload Image",type=['png','jpeg','jpg'])
      if image_file is not None:
    
      # To See Details
      # st.write(type(image_file))
      # st.write(dir(image_file))
        file_details = {"Filename":image_file.name,"FileType":image_file.type,"FileSize":image_file.size}
        vAR_st.write(file_details)

        img = load_image(image_file)
        vAR_st.image(img,width=250)


    elif choice == "Dataset":
      vAR_st.subheader("Dataset")
      data_file = vAR_st.file_uploader("Upload CSV",type=['csv'])
      if vAR_st.button("Process"):
        if data_file is not None:
          file_details = {"Filename":data_file.name,"FileType":data_file.type,"FileSize":data_file.size}
          vAR_st.write(file_details)

          df = pd.read_csv(data_file)
          vAR_st.dataframe(df)

    elif choice == "DocumentFiles":
      vAR_st.subheader("DocumentFiles")
      docx_file = vAR_st.file_uploader("Upload File",type=['txt','docx','pdf'])
      if vAR_st.button("Process"):
        if docx_file is not None:
          file_details = {"Filename":docx_file.name,"FileType":docx_file.type,"FileSize":docx_file.size}
          vAR_st.write(file_details)
        # Check File Type
          if docx_file.type == "text/plain":
    
            vAR_st.text(str(docx_file.read(),"utf-8")) # empty
            raw_text = str(docx_file.read(),"utf-8") # works with st.text and st.write,used for futher processing
            vAR_st.write(raw_text) # works
          elif docx_file.type == "application/pdf":

            try:
              with pdfplumber.open(docx_file) as pdf:
                  page = pdf.pages[0]
                  vAR_st.write(page.extract_text())
            except:
              vAR_st.write("None")
              
          
          elif docx_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        # Use the right file processor ( Docx,Docx2Text,etc)
            raw_text = docx2txt.process(docx_file) # Parse in the uploadFile Class directory
            vAR_st.write(raw_text)

    else:
      vAR_st.subheader("About")
      vAR_st.info("Built with Streamlit")
  


  if __name__ == '__main__':
    main()


  
#Disclaimer.

#we are providing this code block strictly for learning and researching, this is not a production 
#ready code. we have no liability on this particular code under any circumstances; user should
#use this code on their own risk. All software, hardware and other products that are refered 
#in these materials belong to the respective vendor who developed or who owns this product.
