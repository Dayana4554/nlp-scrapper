NLP-enriched News Intelligence Platform

Welcome to the NLP-enriched News Intelligence platform README. This project aims to provide a comprehensive overview of the platform's functionality, components, and usage guidelines. News analysis is an essential part of staying informed in today's world, and this platform offers valuable insights through natural language processing (NLP) techniques.

Project Overview

The NLP-enriched News Intelligence platform is designed to perform the following tasks:

    Connect to a news data source
    Detect entities (specifically, companies and organizations)
    Detect the topic of news articles
    Analyze the sentiment of articles
    Detect environmental scandals related to companies

Components

Scrapper

News Data Source

    To ensure ease of data scraping, we dynamically select a news website for data collection. Frequent changes in website scraping policies necessitate this approach.
    The collected data is stored in two formats: a file system and an optional SQL database.
    Data is stored on a daily basis, including URL, date unique ID, headline, and the body of the article.
    It is recommended to collect data from the past week to manage data volume.

NLP Engine

In a production environment, the NLP engine provides real-time insights based on live-streamed news data. However, to simplify the project, we separate the scrapper and NLP engine components. The scrapper fetches news and stores them, and then the NLP engine processes the stored data.

NLP Processing Steps

    Entities Detection: We aim to detect all entities in the document, with a focus on organizations (ORG). This information should be stored.
        Detect all companies using SpaCy NER on the body of the text. For more information, refer to this guide.

    Topic Detection: The goal is to determine the article's topic (Tech, Sport, Business, Entertainment, or Politics). A labeled dataset is provided to build a classifier. The trained model should be saved as topic_classifier.pkl, along with learning curves plot (learning_curves.png) in the results folder.
        Learning Constraints: Achieve a test score of > 95%.
        Optional: You can train a news topic classifier based on a more challenging dataset, such as the News Category Dataset based on 200k news headlines.

    Sentiment Analysis: Detect the sentiment of news articles using a pre-trained model. NLTK is recommended for this purpose. Save the sentiment results.

    Scandal Detection: Detect environmental disasters related to detected companies using the following methodology:
        Define keywords associated with environmental disasters that may be caused by companies (e.g., pollution, deforestation).
        Compute embeddings of these keywords.
        Compute the distance between keyword embeddings and sentences containing entities.
        Save the distance and flag the top 10 articles with scandals.

    Source Analysis (Optional): Analyze insights about the news sources scraped over at least 5 days. Save plots in the results folder.

Project Structure

The project is organized as follows:

```kotlin

project
│   README.md
│   environment.yml
│
└───data
│   │   topic_classification_data.csv
│
└───results
│   │   topic_classifier.pkl
│   │   learning_curves.png
│   │   enhanced_news.csv
│
└───nlp_engine
│
```

Getting Started

1.Scrapper:

    Run the scrapper until it fetches at least 300 articles:

```bash

python scrapper_news.py
```

Example output:

```php

Scrapping <URL>
Requesting...
Parsing...
Saved in <path>
```

2.NLP Engine:

Process the 300 articles using the NLP engine:

```bash

python nlp_enriched_news.py
```

Example output:

```php

Enriching <URL>:
Cleaning document... (optional)

---------- Detect entities ----------
Detected <X> companies which are <company_1> and <company_2>

---------- Topic detection ----------
Text preprocessing...
The topic of the article is: <topic>

---------- Sentiment analysis ----------
Text preprocessing... (optional)
The title, which is <title>, is <sentiment>
The body of the article is <sentiment>

---------- Scandal detection ----------
Computing embeddings and distance...
Environmental scandal detected for <entity>
```
