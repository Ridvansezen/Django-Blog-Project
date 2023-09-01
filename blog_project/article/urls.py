from django.contrib import admin
from django.urls import path,include
from . import views

app_name = "article"

# Article ile ilgili url'leri burada tanımlıyoruz.
urlpatterns = [
    path('create/', views.createArticle, name="createArticle" ),
]
