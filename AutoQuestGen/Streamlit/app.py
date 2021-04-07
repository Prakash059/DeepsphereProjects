from fill_blank import file_selector,tokenize_sentences,get_noun_adj_verb,get_sentences_for_keyword,get_fill_in_the_blanks
import streamlit as st
import traceback
from PIL import Image
# Utils Pkgs
import codecs
# from true_false import file_selector_tf,tokenize_sentences_tf,pos_tree_from_sentence,get_np_vp,alternate_sentences
import streamlit.components.v1 as stc

def fill_blank(sentence,noun_verbs_adj,keyword_sentence_mapping_noun_verbs_adj):
    text = file_selector()
    st.write('Step 1')
    if st.button('Tokenize sentences'):
        if text is not None:
            with st.spinner("Processing input to tokenize sentence"):
                sentences = tokenize_sentences(text)
                st.write(sentences)
            st.success('Tokenizing completed ')
        else:
            st.error("Please select input file!")
    st.write('Step 2')
    if st.button('Extract Keywords'):
        if text is not None:
            with st.spinner("Processing input to extract keywords"):
                noun_verbs_adj = get_noun_adj_verb(text)
                st.write(noun_verbs_adj)
            st.success('Keywords Extracted')
        else:
            st.error("Please select input file!")
    st.write('Step 3')
    if st.button('Sentence Keyword Match'):
        if text is not None:
            with st.spinner("Processing input to match keywords with sentences"):
                sentences = tokenize_sentences(text)
                noun_verbs_adj = get_noun_adj_verb(text)
                keyword_sentence_mapping_noun_verbs_adj = get_sentences_for_keyword(noun_verbs_adj, sentences)
                st.write(keyword_sentence_mapping_noun_verbs_adj)
            st.success('Sentence Keyword Match Completed')
        else:
            st.error("Please select input file!")
    st.write('Step 4')
    if st.button('Fill in the Blank Questions'):
        if text is not None:
            with st.spinner("Processing input to generate Fill in the blank questions"):
                sentences = tokenize_sentences(text)
                noun_verbs_adj = get_noun_adj_verb(text)
                keyword_sentence_mapping_noun_verbs_adj = get_sentences_for_keyword(noun_verbs_adj, sentences)
                fill_in_the_blanks = get_fill_in_the_blanks(keyword_sentence_mapping_noun_verbs_adj)
                st.write(fill_in_the_blanks)
        else:
            st.error("Please select input file!")

                
def true_false():
    text = file_selector_tf()
    st.write('Step 1')
    if st.button('Tokenize sentences'):
        if text is not None:
            with st.spinner("Processing input to tokenize sentence and get 1st sentence to generate question"):
                sentences = tokenize_sentences_tf(text)
                st.write(sentences)
            st.success('Generated first sentence from given input')
        else:
            st.error("Please select input file!")
    st.write('Step 2')
    if st.button('Words Construction'):
        if text is not None:
            with st.spinner("Parsing input to construct words"):
                sentences = tokenize_sentences_tf(text)
                pos = pos_tree_from_sentence(sentences)
                st.write(pos)
            st.success('Grammatical parsing completed')
        else:
            st.error("Please select input file!")
    st.write('Step 3')     
    if st.button('Sentence Construction'):
        if text is not None:
            with st.spinner("Splitting sentence in-progress"):
                sentences = tokenize_sentences_tf(text)
                pos = pos_tree_from_sentence(sentences)
                split_sentence = get_np_vp(pos,sentences)
                print('split_sentence in app.py- ',split_sentence)
                st.write(split_sentence)
            st.success('Sentence splitted')
        else:
            st.error("Please select input file!")
    st.write('Step 4')    
    if st.button('Alternate Sentences'):
        if text is not None:
            with st.spinner("Generating Alternate sentences"):
                sentences = tokenize_sentences_tf(text)
                pos = pos_tree_from_sentence(sentences)
                alt_sentence = alternate_sentences(pos,sentences)
                st.write(alt_sentence)
        else:
            st.error("Please select input file!")
    
def local_css(file_name):
    
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
        

        
if __name__=='__main__':
    try:
        local_css("style.css")
        
        image = Image.open('DeepSphere_Logo_Final.png')
        st.image(image)
        st.title('NLP Simplifies Questions and Assignments Construction - Powered by GCP')
        activities= ['Fill in the Blank','True or False']
        sentences= []
        noun_verbs_adj=[]
        keyword_sentence_mapping_noun_verbs_adj = {}
        choice = st.sidebar.selectbox('Select Your Question Type',activities)
        st.markdown("""
    <style>
    .css-1aumxhk {
        
        color: black;
        background-color: #4CAF50;
    }
    </style>
""", unsafe_allow_html=True)
        st.sidebar.header("I am up")
        if choice=='Fill in the Blank':
            st.subheader('Fill in the Blank')
            st.markdown('<style>.sidebar .sidebar-content {background-image: linear-gradient(#2e7bcf,#2e7bcf);color: white;</style>',unsafe_allow_html=True)
            fill_blank(sentences,noun_verbs_adj,keyword_sentence_mapping_noun_verbs_adj)
#         if choice=='True or False':
#             st.subheader('True or False')
#             true_false()
    except:
        traceback.print_exc()
