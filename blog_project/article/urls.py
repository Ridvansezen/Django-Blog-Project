from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from . import views

app_name = "article"

# Article ile ilgili url'leri burada tanımlıyoruz.
urlpatterns = [
    path("dashboard/", views.dashboard, name="dashboard"),
    path("addarticle/", views.add_article, name="addArticle"),
    path("article/<int:id>", views.detail_article, name="detailArticle"),
    path("update/<int:id>", views.update_article, name="updateArticle"),
    path("delete/<int:id>", views.delete_article, name="deleteArticle"),
    path("", views.articles, name="articles"),
    path("comment/<int:id>", views.add_comment, name="addComment"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
