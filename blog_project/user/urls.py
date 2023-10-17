from django.urls import include, path

from user import views

app_name = "user"

handler403 = "user.views.handler403"

# User (Kullanıcı) ile ilgili url'leri burada tanımlıyoruz.
urlpatterns = [
    path("register/", views.registerUser, name="registerUser"),
    path("login/", views.loginUser, name="loginUser"),
    path("logout/", views.logoutUser, name="logoutUser"),
    path("profile/", views.profileUser, name="profile"),
    path("settings/", views.settingsUser, name="settings"),
    path('register/', views.registerUser, name="registerUser"),
    path('login/', views.loginUser, name="loginUser"),
    path('logout/', views.logoutUser, name="logoutUser"),
    path('profile/', views.profileUser, name="profile"),
    path('settings/', views.settingsUser, name="settings"),
]
