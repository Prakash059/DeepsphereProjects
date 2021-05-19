import pandas as pd
import numpy as np
import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def chatbot():
    df = pd.read_excel("faq.xlsx")
    df.dropna(inplace=True)
    vectorizer = TfidfVectorizer()   
    vectorizer.fit(np.concatenate((df.Question, df.Answer)))
    Question_vectors = vectorizer.transform(df.Question)
    st.write("You can start chatting with me now.")
    input_question = get_text()
    if True:
        # Read user input
   
        # Locate the closest question
        input_question_vector = vectorizer.transform([input_question])

        # Compute similarities
        similarities = cosine_similarity(input_question_vector, Question_vectors)

        # Find the closest question
        closest = np.argmax(similarities, axis=1)

        # Print the correct answer
        st.write("BOT: " + df.Answer.iloc[closest].values[0])
        
def get_text():
    input_text = st.text_input("")
    return input_text

def main():

    #if st.button("lets talk"):
    chatbot()

if __name__ == '__main__':
    main()