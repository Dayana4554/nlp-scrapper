from textblob import TextBlob

def detect_sentiment(text):
    # Create a TextBlob object
    blob = TextBlob(text)

    # Get the sentiment polarity (-1 to 1)
    sentiment_polarity = blob.sentiment.polarity

    # Classify the sentiment as positive, negative, or neutral
    if sentiment_polarity > 0:
        sentiment = "Positive"
    elif sentiment_polarity < 0:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    return sentiment
