import streamlit as st
import base64
import PyPDF2
from PyPDF2 import PdfFileReader

def read_pdf(datafile):
    pdfReader = PdfFileReader(datafile)
    count = pdfReader.numPages
    all_page_text = ""
    
    for i in range(count):
        page = pdfReader.getPage(i)
        all_page_text += page.extractText()

    return all_page_text 
 
def main():
    datafile = st.sidebar.file_uploader("",type=['pdf'],accept_multiple_files=True)
    # creating a pdf file object
    #if st.button("file"):
        #raw_text=read_pdf(datafile)
        #st.write(raw_text)
    print(type(datafile))
    
if __name__ == '__main__':
    main()
    
    
    