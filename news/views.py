from django.shortcuts import render
from .models import Article

def article_list(request):
    a_list = Article.objects.all()
    context = {"article_list":a_list}
    return render(request, "news/articles.html", context)
