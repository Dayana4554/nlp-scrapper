import spacy


environmental_scandal_keywords = [
    "pollution",
    "deforestation",
    "oil spill",
    "chemical spill",
    "toxic waste",
    "hazardous materials",
    "air pollution",
    "water contamination",
    "wildfire",
    "flood",
    "hurricane",
    "earthquake",
    "tsunami",
    "drought",
    "melting ice",
    "climate change",
    "natural disaster",
    "ecological crisis",
    "nuclear disaster",
    "radiation leak",
    "oil rig explosion",
    "industrial accident",
    "environmental damage",
    "ecosystem collapse",
    "biodiversity loss",
    "ozone depletion",
    "sea level rise",
    "extreme weather",
    "land degradation",
    "mass extinction",
]

def scandal_detection(text):
    # Load spaCy English model
    nlp = spacy.load("en_core_web_sm")

    # Process the text using spaCy
    doc = nlp(text.lower())  # Convert to lowercase for case-insensitive matching

    # Check for the presence of environmental scandal keywords
    detected_keywords = [token.text for token in doc if token.text in environmental_scandal_keywords]

    # Determine if the text is a potential environmental scandal based on the number of detected keywords
    is_scandal = len(detected_keywords) > 0

    return is_scandal