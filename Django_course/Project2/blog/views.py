from django.shortcuts import render
from .models import Article


def article_list(request):
    articles = Article.objects.filter(published=True)
    context = {"articles": articles, "page_title": "articles list"}
    return render(request, "blog/article_list.html", context)
