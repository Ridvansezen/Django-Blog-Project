from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from article import views

# Here we define the main URLs.
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("articles/", include("article.urls")),
    path("user/", include("user.urls")),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
