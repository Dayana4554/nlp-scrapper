import os
import pandas as pd
from scrapper import scrapper_news
from nlp_engine.detect_organisation import detect_organizations
from newsplease import NewsPlease
from nlp_engine.topic_detection import topics, detect_topics
from nlp_engine.sentiment_detection import detect_sentiment
from nlp_engine.scandal_detection import scandal_detection

# Définir le chemin du projet
#project_dir = '/home/student/Zone01/spé-ia/nlp-scrapper'


detect_topics()

#scrapped_data_path = f'{project_dir}/data/guardian_data.csv'
news_data = pd.read_csv('data/guardian_data.csv')

# Parcourir chaque article et appliquer les traitements NLP
for index, row in news_data.iterrows():
    print()
    print("Enriching ",row['URL'] ," :")
    article = NewsPlease.from_url(row['URL'])
    print()

    print("---------- Detect entities ----------")
    print()
    organizations, long = detect_organizations(article.maintext)
    print("Detected ", long, "companies which are ", organizations)
    print()

    print("---------- Topic detection ----------")
    print()
    print("Text preprocessing ...")
    top = topics(row['Article Body'])
    print("The topic of the article is:", top)
    print()

    print("---------- Sentiment analysis ----------")
    print()
    print("Text preprocessing ...")
    print("The title which is ", article.title, " is ", detect_sentiment(article.title))
    print("The body of the article is ", detect_sentiment(article.maintext))
    print()

    print("---------- Scandal detection ----------")
    print()
    print("Computing embeddings and distance ...")
    if scandal_detection(article.maintext):
        print("Environmental scandal detected.")
    else:
        print("No environmental scandal detected.")
    print()
    print("---")