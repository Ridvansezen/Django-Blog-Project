from django.contrib import admin
from django.urls import path,include
from . import views

app_name = "article"

# Article ile ilgili url'leri burada tanımlıyoruz.
urlpatterns = [
    path('dashboard/', views.dashboard, name="dashboard" ),
    path('addarticle/', views.addArticle, name="addArticle" ),
    path('article/<int:id>', views.detailArticle, name="detailArticle" ),
]
