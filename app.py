import streamlit as st
from PyPDF2 import PdfReader
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.tokenize import sent_tokenize
import nltk

# Download NLTK data
nltk.download('punkt')

# Streamlit app
st.title("Easy Learning - Upload Your Notes")

# File uploader
uploaded_file = st.file_uploader("Upload your notes (PDF)", type="pdf")

if uploaded_file is not None:
    # Extract text from PDF
    pdf_reader = PdfReader(uploaded_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    
    # Display the extracted text
    st.write("Extracted Text:")
    st.write(text)

    # Generate summary using TF-IDF
    st.write("Summary:")
    try:
        sentences = sent_tokenize(text)
        vectorizer = TfidfVectorizer()
        tfidf_matrix = vectorizer.fit_transform(sentences)
        sentence_scores = tfidf_matrix.sum(axis=1)
        top_sentences = [sentences[i] for i in sentence_scores.argsort(axis=0)[-3:]]
        summary = " ".join(top_sentences)
        st.write(summary)
    except Exception as e:
        st.error(f"Error generating summary: {e}")