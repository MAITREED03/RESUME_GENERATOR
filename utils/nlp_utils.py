import spacy

# Load spaCy model
nlp = spacy.load("en_core_web_md")

def extract_entities(text):
    doc = nlp(text)
    return [ent.text for ent in doc.ents]