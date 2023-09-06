from django.shortcuts import render,redirect, get_object_or_404
from .forms import ArticleForm
from django.contrib import messages
from .models import Article

def index(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def dashboard(request):
    articles = Article.objects.filter(author = request.user)
    context = {
        "articles":articles,
    }
    return render(request, "articles/dashboard.html", context)

def addArticle(request):
    form = ArticleForm(request.POST or None,request.FILES or None)

    if form.is_valid():
        article = form.save(commit=False)
        article.author = request.user
        article.save()
        messages.success(request, "Makale başarıyla oluşturuldu")
        return redirect("article:dashboard")

    return render(request, "articles/addArticle.html", {"form":form})

def detailArticle(request, id):
    article = get_object_or_404(Article, id = id)
    return render(request, "articles/detailArticle.html", {"article":article})
