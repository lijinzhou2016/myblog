from django.http import HttpResponse
from django.shortcuts import render
from blog.models import Article


def index(request):
    articles = Article.objects.all()
    return render(request, "index.html", {"articles": articles})


def article_page(request, article_id):
    article = Article.objects.get(id=article_id)
    return render(request, "article-detail.html", {"article": article})


def edit_page(request, article_id):
    if int(article_id) > 0:
        article = Article.objects.get(id=article_id)
        return render(request, 'article-edit.html', {"article": article})
    return render(request, 'article-edit.html')


def edit_action(request):
    title = request.POST.get("title", "")
    content = request.POST.get("content", "")
    id = int(request.POST.get("id"))
    if id == 0:
        if title != "" and content != "":
            Article.objects.create(title=title, content=content)
        return index(request)

    article = Article.objects.get(id=id)
    article.title = title
    article.content = content
    article.save()
    articles = Article.objects.all()
    return render(request, 'index.html', {"articles": articles})