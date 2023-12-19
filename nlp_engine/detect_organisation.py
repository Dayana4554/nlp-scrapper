# Import necessary libraries
from bs4 import BeautifulSoup
import pandas as pd
from newsplease import NewsPlease
import json
import requests
import csv
import spacy

nlp = spacy.load('en_core_web_sm')

csv_file = open('result/detect_organisation.csv', 'w', newline='', encoding='utf-8')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['ORG'])

# Function to detect organizations
def detect_organizations(text):
    if text is None:
        return []  # Return an empty list if the text is None

    # Process the text using SpaCy
    doc = nlp(text)

    # Extract organizations (ORG entities)
    organizations = [entity.text for entity in doc.ents if entity.label_ == 'ORG']
     # Utiliser un ensemble pour éliminer les doublons
    unique_set = set(organizations)

    # Convertir l'ensemble en liste pour obtenir l'ordre d'origine
    unique_list = list(unique_set)


    csv_writer.writerow([unique_list])

    result_string = " and ".join(unique_list)

    return result_string, len(unique_list)

