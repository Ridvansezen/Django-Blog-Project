from django.contrib import messages
from django.contrib.auth import (authenticate, login, logout,\
                                 update_session_auth_hash)
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.csrf import csrf_exempt
from django_ratelimit.decorators import ratelimit
from django_ratelimit.exceptions import Ratelimited
from .forms import login_form, register_form


@ratelimit(key="user", rate="5/10minute", method="POST", block=True) # This decorator adds throttling to the register form.
@csrf_exempt
# This function registers the user in the database. And the user is registered.
def register_user(request):
    form = register_form(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        try:
            newUser = User(username=username)
            newUser.set_password(password)
            newUser.save()
            login(request, newUser)
            messages.success(request, "Başarıyla kayıt oldunuz...")
            return redirect("index")
        except IntegrityError:
            messages.info(request, "Bu kullanıcı adı zaten alınmış.")

    context = {
        "form": form,
    }
    return render(request, "user/register.html", context)


@ratelimit(key="user", rate="5/5minute", method="POST", block=True) # This decorator adds throttling to the login form.
@csrf_exempt
# This function logins the user.
def login_user(request):
    form = login_form(request.POST or None)
    context = {"form": form}

    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = authenticate(username=username, password=password)

        if user is None:
            messages.info(request, "Kullanıcı adı veya Parola hatalı.")
        else:
            messages.success(request, "Başarıyla giriş yaptınız...")
            login(request, user)
            return redirect("index")

    return render(request, "user/login.html", context)


# This function changes the 403 page.
def handler403(request, exception):
    return render(request, "403.html", {})




# This function logouts the user.
def logout_user(request):

    logout(request)
    messages.success(request, "Başarıyla çıkış yaptınız...")
    return redirect("index")


# This function shows the clicked user profile page. But it's not working \
#  properly at the moment.
def profile_user(request):
    user = request.user
    registration_date = user.date_joined

    context = {
        "user": user,
        "registration_date": registration_date,
    }

    return render(request, "user/profile.html", context)


# This function shows settings page. In settings page, you can change your \
#  username.
def settings_user(request):
    if request.method == "POST":
        user_change_form = UserChangeForm(request.POST, instance=request.user)
        if user_change_form.is_valid():
            user_change_form.save()
            messages.success(request, "Başarıyla çıkış yaptınız...")
            return redirect("index")
    else:
        user_change_form = UserChangeForm(instance=request.user)

    context = {
        "user_change_form": user_change_form,
    }

    return render(request, "user/settings.html", context)
