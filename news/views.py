from django.shortcuts import render
from .models import Article
from django.contrib.auth import get_user_model

User = get_user_model()

if not User.objects.filter(username='your_username').exists():
    User.objects.create_superuser('your_username', 'your_email@example.com', 'your_password')


def article_list(request):
    a_list = Article.objects.all()
    context = {"article_list":a_list}
    return render(request, "news/articles.html", context)
