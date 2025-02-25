from transformers import pipeline

# Load Hugging Face text generation pipeline
generator = pipeline("text-generation", model="gpt2")

def generate_cover_letter(resume_text, job_description):
    # Generate tailored cover letter
    tailored_cover_letter = generator(
        f"Write a cover letter based on the resume and job description: {resume_text}",
        max_new_tokens=200,  # Generate up to 200 new tokens
    )[0]["generated_text"]
    return tailored_cover_letter