import spacy
import numpy as np
import faiss

# Load spaCy model
nlp = spacy.load("en_core_web_md")

def match_keywords(resume_text, job_description):
    # Extract keywords
    resume_keywords = [token.text for token in nlp(resume_text) if token.is_alpha and not token.is_stop]
    job_keywords = [token.text for token in nlp(job_description) if token.is_alpha and not token.is_stop]

    # Convert keywords to embeddings
    resume_embeddings = np.array([nlp(keyword).vector for keyword in resume_keywords])
    job_embeddings = np.array([nlp(keyword).vector for keyword in job_keywords])

    # Build FAISS index
    dimension = 300
    faiss_index = faiss.IndexFlatL2(dimension)
    faiss_index.add(job_embeddings)

    # Find matches
    distances, indices = faiss_index.search(resume_embeddings, k=1)
    matched_keywords = [job_keywords[idx] for idx in indices.flatten()]
    return matched_keywords