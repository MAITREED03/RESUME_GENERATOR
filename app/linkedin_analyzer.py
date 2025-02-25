import spacy

# Load spaCy model
nlp = spacy.load("en_core_web_md")

def analyze_linkedin_profile(profile_text):
    doc = nlp(profile_text)
    skills = [ent.text for ent in doc.ents if ent.label_ == "ORG"]  # Example: Extract organizations as skills
    suggestions = f"Consider adding more skills: {', '.join(skills)}"
    return suggestions