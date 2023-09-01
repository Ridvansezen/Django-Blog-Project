from django.urls import path,include
from user import views

app_name = "user"

# User (Kullanıcı) ile ilgili url'leri burada tanımlıyoruz.
urlpatterns = [
    path('register/', views.registerUser, name="registerUser"),
    path('login/', views.loginUser, name="loginUser"),
    path('logout/', views.logoutUser, name="logoutUser"),
]
