from django.core.management.base import BaseCommand
from articles.models import Article
from articles.utils import fetch_and_analyze_news

class Command(BaseCommand):
    help = 'Fetches news articles from NewsAPI and stores them with sentiment analysis'

    def add_arguments(self, parser):
        parser.add_argument('api_key', type=str, help='API Key for NewsAPI')

    def handle(self, *args, **options):
        api_key = options['api_key']
        articles = fetch_and_analyze_news(api_key)

        for article_data in articles:
            article, created = Article.objects.update_or_create(
                url=article_data['url'],
                defaults={
                    'title': article_data['title'],
                    'description': article_data['description'],
                    'published_at': article_data['publishedAt'],
                    'source_name': article_data['source']['name'],
                    'sentiment_score': article_data['sentiment']['compound'],
                    'sentiment_comparative': (article_data['sentiment']['pos'] - article_data['sentiment']['neg']),
                    'sentiment_classification': 'positive' if article_data['sentiment']['compound'] > 0 else 'negative' if article_data['sentiment']['compound'] < 0 else 'neutral',
                }
            )

            if created:
                self.stdout.write(self.style.SUCCESS(f'Successfully added new article: {article.title}'))
            else:
                self.stdout.write(self.style.WARNING(f'Updated existing article: {article.title}'))
