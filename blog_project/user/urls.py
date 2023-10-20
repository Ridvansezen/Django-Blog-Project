from django.urls import include, path

from user import views

app_name = "user"

handler403 = "user.views.handler403"

# We define User related urls here.
urlpatterns = [
    path('register/', views.register_user, name="registerUser"),
    path('login/', views.login_user, name="loginUser"),
    path('logout/', views.logout_user, name="logoutUser"),
    path('profile/', views.profile_user, name="profile"),
    path('settings/', views.settings_user, name="settings"),
]
