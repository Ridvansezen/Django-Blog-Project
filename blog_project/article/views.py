from django.contrib import messages
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render, reverse
from .forms import article_form, comment_form
from .models import Article, Comment

# This function is used to show articles.
def articles(request):
    keyword = request.GET.get("keyword")

    if keyword:
        articles = Article.objects.filter(
            Q(title__contains=keyword) | Q(description__contains=keyword)
        )
        return render(request, "articles/articles.html", 
                      {"articles": articles})

    articles = Article.objects.all()

    return render(request, "articles/articles.html", {"articles": articles})

# This function is used to show home page.
def index(request):
    return render(request, "index.html")

# This function is used to show about page.
def about(request):
    return render(request, "about.html")

# This function is used to show the dashboard page. With this function you can \
#  only show your own articles.
def dashboard(request):
    if not request.user.is_authenticated:
        messages.info(request, "Bu sayfaya erişmek için giriş yapmalısınız.")
        return redirect("user:loginUser")

    articles = Article.objects.filter(author=request.user)
    context = {
        "articles": articles,
    }

    return render(request, "articles/dashboard.html", context)

# This function is used to add articles.
def add_article(request):
    if not request.user.is_authenticated:
        messages.info(request, "Bu sayfaya erişmek için giriş yapmalısınız.")
        return redirect("user:loginUser")

    form = article_form(request.POST or None, request.FILES or None)

    if form.is_valid():
        article = form.save(commit=False)
        article.author = request.user
        article.save()
        messages.success(request, "Makale başarıyla oluşturuldu")
        return redirect("article:dashboard")

    return render(request, "articles/addArticle.html", {"form": form})

# This function is used to show articles in detail page.
def detail_article(request, id):
    article = get_object_or_404(Article, id=id)
    comments = article.comments.all()
    return render(
        request,
        "articles/detailArticle.html",
        {"article": article, "comments": comments},
    )

# This function is used to update articles.
def update_article(request, id):
    if not request.user.is_authenticated:
        messages.info(request, "Bu sayfaya erişmek için giriş yapmalısınız.")
        return redirect("user:loginUser")

    article = get_object_or_404(Article, id=id)
    form = article_form(request.POST or None, request.FILES or None, 
                        instance=article)
    if form.is_valid():
        article = form.save(commit=False)
        article.author = request.user
        article.save()
        messages.success(request, "Makale başarıyla güncellendi")
        return redirect("article:dashboard")

    return render(request, "articles/updateArticle.html", {"form": form})

# This function is used to delete articles.
def delete_article(request, id):
    if not request.user.is_authenticated:
        messages.info(request, "Bu sayfaya erişmek için giriş yapmalısınız.")
        return redirect("user:loginUser")

    article = get_object_or_404(Article, id=id)
    article.delete()
    messages.success(request, "Makale başarıyla silindi")
    return redirect("article:dashboard")

# This function is used to add comments in articles.
def add_comment(request, id):
    article = get_object_or_404(Article, id=id)

    if request.method == "POST":
        if not request.user.is_authenticated:
            messages.info(request, 
                          "Yorum yapabilmek için giriş yapmalısınız.")
            return redirect("user:loginUser")

        form = comment_form(request.POST or None)

        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.article = article
            new_comment.comment_author = request.user
            new_comment.save()
            return redirect(reverse("article:detailArticle", 
                                    kwargs={"id": id}))
    else:
        form = comment_form()

    return render(request, "index.html", {"form": form})
