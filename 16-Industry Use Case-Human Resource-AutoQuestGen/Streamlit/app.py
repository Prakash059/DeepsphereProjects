  
import streamlit as st
import traceback
from PIL import Image
# Utils Pkgs
import codecs
import streamlit.components.v1 as stc
import textwrap
import base64
from datetime import datetime
from true_false import tokenize_sentences_tf,pos_tree_from_sentence,get_np_vp,alternate_sentences#,file_selector_tf
from fill_blank import tokenize_sentences,get_noun_adj_verb,get_sentences_for_keyword,get_fill_in_the_blanks,file_selector,download_link
from matchthefollowing import tokenize_sentences, get_keywords,get_sentences_for_keyword,question#,file_selector

def main_file_selector():
    file = st.file_uploader('Upload the text file',type=['txt'])
    if file is not None:
        text = file.read().decode("utf-8")
        st.write('Selected file content is `%s`' % text)
        return text

def dtime():
      return datetime.now().strftime('%Y-%m-%d %H:%M:%S')

def output_file(out, quest_type):
      with open("output.txt","a",encoding="utf-8") as f:
        if quest_type == "Input Text":
              f.write("="*100+"\n")
        else:
              f.write("-"*100+"\n")
        dt = dtime()
        f.write(f"{dt} {quest_type}:\n")
        f.write("-"*100+"\n\n")
        if quest_type == "Input Text" or quest_type == "Match the Following":
              f.write(f"{out}\n")
        elif quest_type == "Fill in The Blanks":
            
            for i,sent in enumerate(out["sentences"]):
                f.write(f"{str(i+1)}. {sent}\n")
            f.write("\n"+str(out["keys"])+"\n")
        else:
            for i,que in enumerate(out):
                f.write(f"{str(i+1)}. {que}\n")
        f.write("\n")

def match_the_foll():
    text = file_selector()
    quest = "Match the Following"
    ts_col1,ts_col2,ts_col3 = st.beta_columns((1,1,2))
    ts_col1.success("Run Model")
    ts_col2.success("Step 1")
    if ts_col3.button('Tokenize sentences'):
        if text is not None:
            with st.spinner("Processing input to tokenize sentence"):
                sentences = tokenize_sentences(text)
                st.write(sentences)
            st.success('Tokenizing completed ')
        else:
            st.error("Please select input file!")
    ek_col1,ek_col2,ek_col3 = st.beta_columns((1,1,2))
    ek_col1.success("Run Model")
    ek_col2.success("Step 2")
    if ek_col3.button('Extract Keywords'):
        if text is not None:
            with st.spinner("Processing input to extract keywords"):
                keywords = get_keywords(text)[:6]
                st.write(keywords)
            st.success('Keywords Extracted')
        else:
            st.error("Please select input file!")
    km_col1,km_col2,km_col3 = st.beta_columns((1,1,2))
    km_col1.success("Run Model")
    km_col2.success("Step 3")
    if km_col3.button('Sentence Keyword Match'):
        if text is not None:
            with st.spinner("Processing input to match keywords with sentences"):
                sentences = tokenize_sentences(text)
                keywords = get_keywords(text)[:6]
                keyword_sentence_mapping = get_sentences_for_keyword(keywords, sentences)
                st.write(keyword_sentence_mapping)
            st.success('Sentence Keyword Match Completed')
        else:
            st.error("Please select input file!")
    fq_col1,fq_col2,fq_col3 = st.beta_columns((1,1,2))
    fq_col1.success("Run Model")
    fq_col2.success("Step 4")
    if fq_col3.button('Match the Following Questions'):
        if text is not None:
            with st.spinner("Processing input to generate questions"):
                sentences = tokenize_sentences(text)
                keywords = get_keywords(text)[:6]
                keyword_sentence_mapping = get_sentences_for_keyword(keywords, sentences)
                mtf_table, ptable = question(keyword_sentence_mapping)
                # st.write(mtf_table)
                st.table(mtf_table)
                output_file(text,"Input Text")
                output_file(ptable, quest)
        else:
            st.error("Please select input file!")
    vm_col1,vm_col2,vm_col3 = st.beta_columns((1,1,2))
    vm_col1.success("Validate Model")
    vm_col2.success("Step 5")
    if vm_col3.button('View Model Outcome'):
        if text is not None:
#             pass
            sentences = tokenize_sentences(text)
            keywords = get_keywords(text)[:6]
            keyword_sentence_mapping = get_sentences_for_keyword(keywords, sentences)
            mtf_table = question(keyword_sentence_mapping)
            st.markdown(download_link(mtf_table, 'model_output.txt', 'Click here to download your output!',quest),unsafe_allow_html=True)
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
    ts_col1,ts_col2,ts_col3 = st.beta_columns((1,1,2))
    ts_col1.success("Run Model")
    ts_col2.success("Step 1")
    if ts_col3.button('Tokenize sentences'):
        if text is not None:
            with st.spinner("Processing input to tokenize sentence"):
                sentences = tokenize_sentences(text)
                st.write(sentences)
            st.success('Tokenizing completed ')
        else:
            st.error("Please select input file!")
    ek_col1,ek_col2,ek_col3 = st.beta_columns((1,1,2))
    ek_col1.success("Run Model")
    ek_col2.success("Step 2")
    if ek_col3.button('Extract Keywords'):
        if text is not None:
            with st.spinner("Processing input to extract keywords"):
                noun_verbs_adj = get_noun_adj_verb(text)
                st.write(noun_verbs_adj)
            st.success('Keywords Extracted')
        else:
            st.error("Please select input file!")
    sk_col1,sk_col2,sk_col3 = st.beta_columns((1,1,2))
    sk_col1.success("Run Model")
    sk_col2.success("Step 3")
    if sk_col3.button('Sentence Keyword Match'):
        if text is not None:
            with st.spinner("Processing input to match keywords with sentences"):
                sentences = tokenize_sentences(text)
                noun_verbs_adj = get_noun_adj_verb(text)
                keyword_sentence_mapping_noun_verbs_adj = get_sentences_for_keyword(noun_verbs_adj, sentences)
                st.write(keyword_sentence_mapping_noun_verbs_adj)
            st.success('Sentence Keyword Match Completed')
        else:
            st.error("Please select input file!")
    fb_col1,fb_col2,fb_col3 = st.beta_columns((1,1,2))
    fb_col1.success("Run Model")
    fb_col2.success("Step 4")
    if fb_col3.button('Fill in the Blank Questions'):
        if text is not None:
            with st.spinner("Processing input to generate Fill in the blank questions"):
                sentences = tokenize_sentences(text)
                noun_verbs_adj = get_noun_adj_verb(text)
                keyword_sentence_mapping_noun_verbs_adj = get_sentences_for_keyword(noun_verbs_adj, sentences)
                fill_in_the_blanks = get_fill_in_the_blanks(keyword_sentence_mapping_noun_verbs_adj)
                st.write(fill_in_the_blanks)
                output_file(text,"Input Text")
                output_file(fill_in_the_blanks, quest)
        else:
            st.error("Please select input file!")
    vm_col1,vm_col2,vm_col3 = st.beta_columns((1,1,2))
    vm_col1.success("Validate Model")
    vm_col2.success("Step 5")
    if vm_col3.button('View Model Outcome'):
        if text is not None:
#             pass
            sentences = tokenize_sentences(text)
            noun_verbs_adj = get_noun_adj_verb(text)
            keyword_sentence_mapping_noun_verbs_adj = get_sentences_for_keyword(noun_verbs_adj, sentences)
            fill_in_the_blanks = get_fill_in_the_blanks(keyword_sentence_mapping_noun_verbs_adj)
            st.markdown(download_link(fill_in_the_blanks, 'model_output.txt', 'Click here to download your output!',quest),unsafe_allow_html=True)
        else:
            st.error("Please select input file!")

                
def true_false():
    text = file_selector()
    quest = "True or False"
    ts_col1,ts_col2,ts_col3 = st.beta_columns((1,1,2))
    ts_col1.success("Run Model")
    ts_col2.success("Step 1")
    if ts_col3.button('Tokenize sentences'):
        if text is not None:
            with st.spinner("Processing input to tokenize sentence and get 1st sentence to generate question"):
                sentences = tokenize_sentences_tf(text)
                st.write(sentences)
            st.success('Generated first sentence from given input')
        else:
            st.error("Please select input file!")
    wc_col1,wc_col2,wc_col3 = st.beta_columns((1,1,2))
    wc_col1.success("Run Model")
    wc_col2.success("Step 2")
    if wc_col3.button('Words Construction'):
        if text is not None:
            with st.spinner("Parsing input to construct words"):
                sentences = tokenize_sentences_tf(text)
                pos = pos_tree_from_sentence(sentences)
                st.write(pos)
            st.success('Grammatical parsing completed')
        else:
            st.error("Please select input file!")
    sc_col1,sc_col2,sc_col3 = st.beta_columns((1,1,2))
    sc_col1.success("Run Model")
    sc_col2.success("Step 3")
    if sc_col3.button('Sentence Construction'):
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
    as_col1,as_col2,as_col3 = st.beta_columns((1,1,2))
    as_col1.success("Run Model")
    as_col2.success("Step 4")
    if as_col3.button('Alternate Sentences'):
        if text is not None:
            with st.spinner("Generating Alternate sentences"):
                sentences = tokenize_sentences_tf(text)
                pos = pos_tree_from_sentence(sentences)
                alt_sentence = alternate_sentences(pos,sentences)
                st.write(alt_sentence)
                output_file(text,"Input Text")
                output_file(alt_sentence,quest)
        else:
            st.error("Please select input file!")
    vm_col1,vm_col2,vm_col3 = st.beta_columns((1,1,2))
    vm_col1.success("Validate Model")
    vm_col2.success("Step 5")
    if vm_col3.button('View Model Outcome'):
        if text is not None:
#             pass
            sentences = tokenize_sentences_tf(text)
            pos = pos_tree_from_sentence(sentences)
            alt_sentence = alternate_sentences(pos,sentences)
            st.markdown(download_link(alt_sentence, 'model_output.txt', 'Click here to download your output!',quest),unsafe_allow_html=True)
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
    st.markdown('<hr style="border-top: 6px solid #8c8b8b; width: 150%;margin-left:-180px">',unsafe_allow_html=True)
    activities= ['Select Your Question Type','Fill in the Blanks','True or False', 'Match the Following', 'MCQ']
    model_choices = ['Model Implemented','BERT']
    libraries = ['Library Used','spacy','nltk','tensorflow','allennlp','flashtext','streamlit','pke']
    gcp = ['GCP Services Used','VM Instance','Compute Engine']
    choice = st.sidebar.selectbox('',activities)
    model_choice = st.sidebar.selectbox('',model_choices)
    libraries_choice = st.sidebar.selectbox('',libraries)
    gcp_services = st.sidebar.selectbox('',gcp)
    return choice

if __name__=='__main__':
    try:
        choice = all_initialisations()
        sentences= []
        noun_verbs_adj=[]
        keyword_sentence_mapping_noun_verbs_adj = {}
#         main_text = main_file_selector()
#         if main_text:
#             output_file(main_text,"Input Text")
        if choice=='Fill in the Blanks':
            st.subheader(choice)
            fill_blank( sentences,noun_verbs_adj,keyword_sentence_mapping_noun_verbs_adj)
        if choice=='True or False':
            st.subheader(choice)
            true_false()
        if choice == 'Match the Following':
            st.subheader(choice)
            match_the_foll()
        if choice == 'MCQ':
            st.subheader('Multiple Choice Questions')
            mcq()
    except:
        traceback.print_exc()