from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns
import os as os
import pandas as pd
from sklearn.model_selection import learning_curve
import numpy as np
from sklearn.pipeline import Pipeline
import joblib

def detect_topics():

    # Read the dataset
    df = pd.read_csv('result/bbc_train.csv')

    X_train, X_test, y_train, y_test = train_test_split(df['Text'], df['Category'], test_size=0.2, random_state=42)

    # Définissez le pipeline
    pipeline = Pipeline([
        ('tfidf', TfidfVectorizer(max_features=5000)),
        ('clf', MultinomialNB())
    ])

    # Entraînez le modèle avec le pipeline
    pipeline.fit(X_train, y_train)

    # Faites des prédictions
    y_pred = pipeline.predict(X_test)

    # Évaluez le modèle
    accuracy = accuracy_score(y_test, y_pred)

    pipeline.fit(X_train, y_train)

    joblib.dump(pipeline, 'result/topic_classifier.pkl')


    # Obtenez les courbes d'apprentissage
    train_sizes, train_scores, test_scores = learning_curve(pipeline, X_train, y_train, cv=5, scoring='accuracy', n_jobs=-1, train_sizes=np.linspace(.1, 1.0, 5))

    # Calculez la moyenne des scores sur les plis de validation
    train_scores_mean = np.mean(train_scores, axis=1)
    test_scores_mean = np.mean(test_scores, axis=1)

    # Tracez la courbe d'apprentissage
    plt.figure(figsize=(10, 6))
    plt.plot(train_sizes, train_scores_mean, label='Train')
    plt.xlabel('Training Size')
    plt.ylabel('Accuracy')
    plt.title('Learning Curve')
    plt.legend()
    plt.grid(True)
    plt.savefig('result/learning_curve.png')

model_path = 'result/topic_classifier.pkl'
pipeline = joblib.load(model_path)

def topics(text):
    predicted_topic = pipeline.predict([text])[0]
    return predicted_topic

