# AI-Powered Resume & Cover Letter Generator

This project is a web application that generates **tailored resumes and cover letters** based on job descriptions, optimized for **Applicant Tracking Systems (ATS)**. It also includes a feature to analyze LinkedIn profiles and suggest improvements.

---

## Features

- **Resume Tailoring**: Generates ATS-optimized resumes based on job descriptions.
- **Cover Letter Generation**: Creates personalized cover letters tailored to specific job descriptions.
- **LinkedIn Profile Analysis**: Analyzes LinkedIn profiles and provides improvement suggestions.
- **Keyword Matching**: Matches keywords between resumes and job descriptions for better alignment.

---

## Tech Stack

- **Frontend**: Streamlit
- **Backend**: Python
- **NLP**: spaCy, Hugging Face Transformers
- **Vector Database**: FAISS
- **Templates**: Microsoft Word (`.docx`)

---

## Folder Structure

resume_generator/
├── app/ # Main application code
│ ├── init.py
│ ├── main.py # Streamlit app entry point
│ ├── resume_parser.py # Resume parsing logic
│ ├── cover_letter_generator.py # Cover letter generation logic
│ ├── keyword_matcher.py # Keyword matching logic
│ └── linkedin_analyzer.py # LinkedIn profile analysis logic
├── data/ # Sample data for testing
│ ├── resumes/ # Sample resumes
│ ├── job_descriptions/ # Sample job descriptions
│ └── linkedin_profiles/ # Sample LinkedIn profiles
├── models/ # Pre-trained models
│ ├── spacy/ # spaCy models (e.g., en_core_web_md)
│ └── transformers/ # Hugging Face models (e.g., GPT-2)
├── templates/ # Resume and cover letter templates
│ ├── resume_template.docx # ATS-friendly resume template
│ └── cover_letter_template.docx # ATS-friendly cover letter template
├── tests/ # Unit and integration tests
│ ├── test_resume_parser.py # Tests for resume parsing
│ ├── test_cover_letter_gen.py # Tests for cover letter generation
│ └── test_keyword_matcher.py # Tests for keyword matching
├── utils/ # Utility functions
│ ├── file_utils.py # File handling utilities
│ ├── nlp_utils.py # NLP-related utilities
│ └── logging_utils.py # Logging configuration
├── requirements.txt # Python dependencies
├── README.md # Project documentation
└── .gitignore # Files/folders to ignore in Git



---

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/MAITREED03/resume_generator.git
cd resume_generator


2. Install Dependencies
pip install -r requirements.txt

3. Download spaCy Model
python -m spacy download en_core_web_md

4. Run the Application
streamlit run app/main.py

Usage
Upload Your Resume:

Upload a PDF resume using the file uploader.

Paste Job Description:

Paste the job description into the text area.

Generate Tailored Resume and Cover Letter:

The app will generate a tailored resume and cover letter based on the job description.

Analyze LinkedIn Profile:

Paste your LinkedIn profile text to receive improvement suggestions.


License
This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgments
spaCy: For NLP tasks.

Hugging Face: For text generation models.

Streamlit: For building the web app.