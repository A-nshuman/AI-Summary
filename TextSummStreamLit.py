import streamlit as st
from transformers import pipeline

st.header("Text Summarizer")

text = st.text_area("Enter text to Summarize")

summarizer = pipeline('summarization', model = "sshleifer/distilbart-cnn-12-6")

summary = summarizer(text, max_length = 130, min_length = 30, do_sample = False)

summary_text = summary[0]['summary_text']

if st.button("Summarize"):
    st.write(summary_text)