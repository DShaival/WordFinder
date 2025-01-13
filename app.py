import streamlit as st

from main import find_suggested_words

word = st.text_input("Enter a word")
word_length = st.number_input("Enter length of the word", min_value=0, step=1, value=0, format='%d')
exculded_letters = st.text_input("Enter letters to exclude",placeholder="Eg: abcd...")

submit = st.button("Submit")

if submit and word == "":
    st.write("Please enter a word")

if submit and word_length == 0:
    st.write("Please enter the length of the word")
    
if submit:
    suggested_words = find_suggested_words(word, exculded_letters, word_length)
    if(suggested_words=={"error": "word length is greater than the length of the input word"}):
        st.write("Word length is greater than the length of the input word")
    else:    
        st.write("Suggested words:")
        for word in suggested_words:
            st.write(word)
    