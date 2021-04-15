import streamlit as st
import traceback
from PIL import Image
# Utils Pkgs
import codecs
import streamlit.components.v1 as stc
import textwrap
from datetime import datetime
from true_false import file_selector_tf,tokenize_sentences_tf,pos_tree_from_sentence,\
    get_np_vp,alternate_sentences
from fill_blank import file_selector,tokenize_sentences,get_noun_adj_verb,\
    get_sentences_for_keyword,get_fill_in_the_blanks
from matchthefollowing import tokenize_sentences, get_keywords, \
    get_sentences_for_keyword,question,file_selector

def output_file(out_var,quest_type):
    dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open("output.txt","a") as f:
        f.write(f"{dt} {quest_type} OUTPUT: {out_var}")
        f.write("\n\n")


def match_the_foll():
    text = file_selector()
    quest = "Match the Following"
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
                keywords = get_keywords(text)[:6]
                st.write(keywords)
            st.success('Keywords Extracted')
        else:
            st.error("Please select input file!")
    st.write('Step 3')
    if st.button('Sentence Keyword Match'):
        if text is not None:
            with st.spinner("Processing input to match keywords with sentences"):
                sentences = tokenize_sentences(text)
                keywords = get_keywords(text)[:6]
                keyword_sentence_mapping = get_sentences_for_keyword(keywords, sentences)
                st.write(keyword_sentence_mapping)
            st.success('Sentence Keyword Match Completed')
        else:
            st.error("Please select input file!")
    st.write('Step 4')
    if st.button('Match the Following Questions'):
        if text is not None:
            with st.spinner("Processing input to generate questions"):
                sentences = tokenize_sentences(text)
                keywords = get_keywords(text)[:6]
                keyword_sentence_mapping = get_sentences_for_keyword(keywords, sentences)
                mtf_table = question(keyword_sentence_mapping)
                # st.write(mtf_table)
                st.table(mtf_table)
                output_file(mtf_table, quest)
        else:
            st.error("Please select input file!")

def mcq():
    text = file_selector()
    quest = "MCQ"
    st.write("MCQ question generation pending")
    mcq = "Output Pending"
    output_file(mcq, quest)

def fill_blank(sentence,noun_verbs_adj,keyword_sentence_mapping_noun_verbs_adj):
    text = file_selector()
    quest = "Fill in The Blanks"
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
                output_file(fill_in_the_blanks, quest)
        else:
            st.error("Please select input file!")

                
def true_false():
    text = file_selector_tf()
    quest = "True or False"
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
                output_file(alt_sentence,quest)
        else:
            st.error("Please select input file!")
    
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
        
def all_initialisations():
    local_css("style.css")
    image = Image.open('DeepSphere_Logo_Final.png')
    st.image(image)
    st.markdown('<h2>NLP Simplifies Questions and Assignments Construction <br><font style="color: #5500FF;">Powered by Google Cloud & Colab</font></h2>',unsafe_allow_html=True)
    activities= ['Fill in the Blank','True or False', 'Match the Following', 'MCQ']
    choice = st.sidebar.selectbox('Select Your Question Type',activities)

if __name__=='__main__':
    try:
        all_initialisations()
        sentences= []
        noun_verbs_adj=[]
        keyword_sentence_mapping_noun_verbs_adj = {}
        if choice=='Fill in the Blank':
            st.subheader('Fill in the Blank')
            fill_blank(sentences,noun_verbs_adj,keyword_sentence_mapping_noun_verbs_adj)
        if choice=='True or False':
            st.subheader('True or False')
            true_false()
        if choice == 'Match the Following':
            st.subheader('Match the Following')
            match_the_foll()
        if choice == 'MCQ':
            st.subheader('Multiple Choice Questions')
            mcq()
    except:
        traceback.print_exc()
