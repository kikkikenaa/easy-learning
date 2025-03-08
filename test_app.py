import streamlit as st

# Streamlit app for file upload
st.title("Easy Learning - Upload Your Notes and Exam Papers")

st.header("Upload Files Here")
notes_files = st.file_uploader("Upload your notes (PDF)", type="pdf", accept_multiple_files=True)
exam_files = st.file_uploader("Upload exam papers (PDF)", type="pdf", accept_multiple_files=True)

# Store uploaded files in session state
if notes_files:
    st.session_state["notes_files"] = notes_files
    st.success(f"Uploaded {len(notes_files)} notes file(s) successfully!")

if exam_files:
    st.session_state["exam_files"] = exam_files
    st.success(f"Uploaded {len(exam_files)} exam paper(s) successfully!")
