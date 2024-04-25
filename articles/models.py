from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    url = models.URLField(max_length=500)
    published_at = models.DateTimeField()
    source_name = models.CharField(max_length=100)
    sentiment_score = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    sentiment_comparative = models.DecimalField(max_digits=5, decimal_places=3, default=0.00)
    sentiment_classification = models.CharField(max_length=50, default='neutral')

    def __str__(self):
        return self.title
