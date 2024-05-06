import requests
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk
from django.utils.timezone import make_aware
from datetime import datetime

# Ensure nltk data is downloaded
nltk.download('vader_lexicon', quiet=True)

def fetch_news(api_key):
    """Fetch news using the NewsAPI."""
    url = "https://newsapi.org/v2/top-headlines"
    parameters = {
        'country': 'us',
        'apiKey': api_key,
    }
    response = requests.get(url, params=parameters)
    articles = response.json().get('articles', [])
    return articles

def analyze_sentiment(text):
    """Analyze sentiment of the text using NLTK."""
    sia = SentimentIntensityAnalyzer()
    sentiment = sia.polarity_scores(text)
    return sentiment

def fetch_news(api_key,query):
    
    url = 'https://newsapi.org/v2/everything'
    params = {
        'q': query,
        'apiKey': api_key,
        'language': 'en',
        'sortBy': 'publishedAt'
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json().get('articles',[])
    else:
        return response.status_code, response.text
    
def fetch_and_analyze_news(api_key):
    articles = fetch_news(api_key, 'Star Wars')
    for article in articles:
        sentiment = analyze_sentiment(
            article['description'] if article['description'] else article['title'])
        article['sentiment'] = sentiment
    return articles

def process_and_load_news(api_key):
    """Fetch news, process them, and load them into the database."""
    articles = fetch_news(api_key, 'Star Wars')
    from .models import Article  # Importing models here to avoid circular imports

    for article_data in articles:
        # Ensuring description is never None and not empty
        description = article_data.get('description') or article_data.get('title') or 'No description available'

        # Parsing publishedAt to datetime, handling None case
        published_at = article_data.get('publishedAt')
        if published_at:
            try:
                published_at = make_aware(datetime.strptime(published_at, '%Y-%m-%dT%H:%M:%SZ'))
            except ValueError:
                published_at = None  # In case the date format is incorrect or missing

        sentiment = analyze_sentiment(description)
        article, created = Article.objects.update_or_create(
            url=article_data['url'],
            defaults={
                'title': article_data['title'],
                'description': description,
                'published_at': published_at,
                'source_name': article_data['source']['name'],
                'sentiment_score': sentiment['compound'],
                'sentiment_comparative': sentiment['pos'] - sentiment['neg'],
                'sentiment_classification': 'positive' if sentiment['compound'] > 0 else 'negative' if sentiment['compound'] < 0 else 'neutral',
            }
        )

