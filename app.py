import streamlit as st
from PyPDF2 import PdfReader
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
import nltk
import string
from collections import Counter
from nltk.stem import WordNetLemmatizer

# Download NLTK data
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

# Streamlit app
st.title("Easy Learning - Analyze Notes and Exam Papers")

# File uploaders
st.sidebar.header("Upload Files")
notes_files = st.sidebar.file_uploader("Upload your notes (PDF)", type="pdf", accept_multiple_files=True)
exam_files = st.sidebar.file_uploader("Upload exam papers (PDF)", type="pdf", accept_multiple_files=True)

# Debugging: Check if files are detected
if notes_files:
    st.success(f"{len(notes_files)} notes file(s) uploaded successfully!")

if exam_files:
    st.success(f"{len(exam_files)} exam paper(s) uploaded successfully!")

# Function to extract text from PDFs
def extract_text_from_pdf(files):
    text = ""
    for file in files:
        try:
            pdf_reader = PdfReader(file)
            for page in pdf_reader.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
        except Exception as e:
            st.error(f"Error reading {file.name}: {e}")
    return text.strip()

# Function to preprocess text
def preprocess_text(text):
    if not text:
        return ""

    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))  # Remove punctuation
    text = ''.join([char for char in text if not char.isdigit()])  # Remove numbers

    tokens = word_tokenize(text)
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [word for word in tokens if word not in stop_words]

    lemmatizer = WordNetLemmatizer()
    lemmatized_tokens = [lemmatizer.lemmatize(word) for word in filtered_tokens]

    return " ".join(lemmatized_tokens)

# Function to analyze exam papers
def analyze_exam_papers(text):
    if not text:
        return []

    sentences = sent_tokenize(text)
    words = word_tokenize(text)
    word_freq = Counter(words)
    
    most_common = word_freq.most_common(10)
    return most_common

# Function to highlight important terms
def highlight_important_areas(notes_text, important_terms):
    highlighted_text = notes_text
    for term, _ in important_terms:
        highlighted_text = highlighted_text.replace(term, f"<b>{term}</b>")
    return highlighted_text

# Process files if both are uploaded
if notes_files and exam_files:
    st.write("Processing files...")

    # Extract text
    notes_text = extract_text_from_pdf(notes_files)
    exam_text = extract_text_from_pdf(exam_files)

    # Preprocess text
    cleaned_notes = preprocess_text(notes_text)
    cleaned_exam = preprocess_text(exam_text)

    # Analyze exam papers
    important_terms = analyze_exam_papers(cleaned_exam)

    if important_terms:
        st.subheader("Frequently Tested Topics:")
        st.write(important_terms)

        # Highlight important areas in notes
        highlighted_notes = highlight_important_areas(notes_text, important_terms)
        st.subheader("Highlighted Notes:")
        st.markdown(highlighted_notes, unsafe_allow_html=True)
    else:
        st.warning("No significant keywords detected in exam papers.")

elif notes_files:
    st.warning("Please upload exam papers to analyze frequently tested topics.")
elif exam_files:
    st.warning("Please upload notes to highlight important areas.")
else:
    st.info("Upload your notes and exam papers to get started.")
