from nltk.sentiment.vader import SentimentIntensityAnalyzer


def analyze_sentiment(text):
    sent_analyzer = SentimentIntensityAnalyzer()
    scores = sent_analyzer.polarity_scores(text)

    if scores['compound'] >= .15:
        sentiment = 'Positive'
    if scores['compound'] <= -.15:
        sentiment = 'Negative'
    else:
        sentiment = 'Neutral'

    return sentiment
