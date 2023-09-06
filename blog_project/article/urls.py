from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "article"

# Article ile ilgili url'leri burada tanımlıyoruz.
urlpatterns = [
    path('dashboard/', views.dashboard, name="dashboard" ),
    path('addarticle/', views.addArticle, name="addArticle" ),
    path('article/<int:id>', views.detailArticle, name="detailArticle" ),
    path('update/<int:id>', views.updateArticle, name="updateArticle" ),
    path('delete/<int:id>', views.deleteArticle, name="deleteArticle" ),
    path('', views.articles, name="articles" ),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
