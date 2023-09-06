from django.shortcuts import render,redirect, get_object_or_404
from .forms import ArticleForm
from django.contrib import messages
from .models import Article
from django.contrib.auth.decorators import login_required

def articles(request):
    articles = Article.objects.all()

    return render(request, "articles/articles.html", {"articles":articles})

def index(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")


def dashboard(request):
    if not request.user.is_authenticated:
        messages.info(request, "Bu sayfaya erişmek için giriş yapmalısınız.")
        return redirect("user:loginUser")
    
    articles = Article.objects.filter(author = request.user)
    context = {
        "articles":articles,
    }

    return render(request, "articles/dashboard.html", context)


def addArticle(request):
    if not request.user.is_authenticated:
        messages.info(request, "Bu sayfaya erişmek için giriş yapmalısınız.")
        return redirect("user:loginUser")
    
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


def updateArticle(request,id):
    if not request.user.is_authenticated:
        messages.info(request, "Bu sayfaya erişmek için giriş yapmalısınız.")
        return redirect("user:loginUser")

    article = get_object_or_404(Article, id=id)
    form = ArticleForm(request.POST or None, request.FILES or None, instance=article)
    if form.is_valid():
        article = form.save(commit=False)
        article.author = request.user
        article.save()
        messages.success(request, "Makale başarıyla güncellendi")
        return redirect("article:dashboard")

    return render(request, "articles/updateArticle.html", {"form":form})


def deleteArticle(request,id):
    if not request.user.is_authenticated:
        messages.info(request, "Bu sayfaya erişmek için giriş yapmalısınız.")
        return redirect("user:loginUser")
    
    article = get_object_or_404(Article, id = id)
    article.delete()
    messages.success(request, "Makale başarıyla silindi")
    return redirect("article:dashboard")