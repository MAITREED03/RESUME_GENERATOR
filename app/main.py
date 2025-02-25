import streamlit as st
import spacy
from transformers import pipeline
import PyPDF2
import numpy as np
import faiss

# Load spaCy model with word vectors
nlp = spacy.load("en_core_web_md")

# Load Hugging Face text generation pipeline
generator = pipeline("text-generation", model="gpt2")

# Initialize FAISS index
dimension = 300  # spaCy word vectors are 300-dimensional

# Function to extract text from PDF
def extract_text_from_pdf(file):
    reader = PyPDF2.PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

# Function to extract keywords using spaCy
def extract_keywords(text):
    doc = nlp(text)
    keywords = [token.text for token in doc if token.is_alpha and not token.is_stop]
    return list(set(keywords))  # Remove duplicates

# Function to match keywords using FAISS
def match_keywords(job_keywords, resume_keywords):
    # Convert keywords to embeddings
    job_embeddings = np.array([nlp(keyword).vector for keyword in job_keywords])
    resume_embeddings = np.array([nlp(keyword).vector for keyword in resume_keywords])

    # Ensure each embedding is 300-dimensional
    if job_embeddings.shape[1] != dimension:
        raise ValueError(f"Job embeddings must have dimensionality {dimension}, but got {job_embeddings.shape[1]}")
    if resume_embeddings.shape[1] != dimension:
        raise ValueError(f"Resume embeddings must have dimensionality {dimension}, but got {resume_embeddings.shape[1]}")

    # Build FAISS index
    faiss_index = faiss.IndexFlatL2(dimension)  # Reinitialize index
    faiss_index.add(job_embeddings)

    # Find matches
    distances, indices = faiss_index.search(resume_embeddings, k=1)
    matched_keywords = [job_keywords[idx] for idx in indices.flatten()]
    return matched_keywords

# Function to generate tailored resume and cover letter
def generate_tailored_content(resume_text, job_description):
    # Extract keywords
    job_keywords = extract_keywords(job_description)
    resume_keywords = extract_keywords(resume_text)

    # Match keywords
    matched_keywords = match_keywords(job_keywords, resume_keywords)

    # Truncate input text if necessary
    max_input_length = 500  # Adjust based on model's token limit
    truncated_resume_text = resume_text[:max_input_length]

    # Generate tailored resume
    tailored_resume = generator(
        f"Rewrite this resume based on the job description: {truncated_resume_text}",
        max_new_tokens=200,  # Generate up to 200 new tokens
    )[0]["generated_text"]

    # Generate tailored cover letter
    tailored_cover_letter = generator(
        f"Write a cover letter based on the resume and job description: {truncated_resume_text}",
        max_new_tokens=200,  # Generate up to 200 new tokens
    )[0]["generated_text"]

    return tailored_resume, tailored_cover_letter, matched_keywords

# Streamlit App
def main():
    st.title("AI-Powered Resume & Cover Letter Generator")
    st.write("Upload your resume and provide a job description to get started.")

    # Upload resume
    resume_file = st.file_uploader("Upload your resume (PDF)", type="pdf")
    if resume_file:
        resume_text = extract_text_from_pdf(resume_file)
        st.write("Resume uploaded successfully!")

        # Input job description
        job_description = st.text_area("Paste the job description here:")

        if job_description:
            # Generate tailored content
            tailored_resume, tailored_cover_letter, matched_keywords = generate_tailored_content(resume_text, job_description)

            # Display results
            st.subheader("Tailored Resume")
            st.write(tailored_resume)

            st.subheader("Tailored Cover Letter")
            st.write(tailored_cover_letter)

            st.subheader("Matched Keywords")
            st.write(", ".join(matched_keywords))

if __name__ == "__main__":
    main()