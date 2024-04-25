from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Article

class ArticleListView(ListView):
    model = Article
    template_name = 'article_list.html'
    context_object_name = 'articles'  # Specifies the name of the variable to use in the template
    ordering = ['-published_at']  # Orders the articles by the published date, newest first

    # Optionally, add custom filtering or other logic
    def get_queryset(self):
        # You can include custom filtering logic here if needed
        return super().get_queryset().filter(sentiment_classification='positive')  # Example: only positive articles


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article_detail.html'
    context_object_name = 'article'  # This is optional if you are okay with the default context name 'object'

    # Optionally, you can add methods to handle other logic, such as logging or additional context
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Example: Add extra context if needed
        # context['extra_info'] = 'This is some extra information'
        return context


# # funciton based
# def article_list(request):
#     articles = Article.objects.all().order_by('-published_at')  # Ordering by the newest first
#     return render(request, 'articles/article_list.html', {'articles': articles})

# def article_detail(request, pk):
#     article = Article.objects.get(pk=pk)
#     return render(request, 'articles/article_detail.html', {'article': article})
