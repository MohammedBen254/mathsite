from django.shortcuts import render
from .models import Article

def article_list(request):
    articles = Article.objects.order_by('-pub_date')[:5]  # Get the 5 latest articles
    return render(request, 'home.html', {'articles': articles})