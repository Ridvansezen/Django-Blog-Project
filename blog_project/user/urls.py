from django.urls import include, path
from django.conf.urls import handler404

from user import views

app_name = "user"

handler403 = "user.views.handler403"
handler404 = "user.views.handler404"

# User (Kullanıcı) ile ilgili url'leri burada tanımlıyoruz.
urlpatterns = [

    path("register/", views.registerUser, name="registerUser"),
    path("login/", views.loginUser, name="loginUser"),
    path("logout/", views.logoutUser, name="logoutUser"),
    path("profile/", views.profileUser, name="profile"),
    path("settings/", views.settingsUser, name="settings"),
]
