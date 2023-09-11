from django.shortcuts import render,redirect
from .forms import RegisterForm, LoginForm
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

def registerUser(request):
    form = RegisterForm(request.POST or None)
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

def loginUser(request):
    form = LoginForm(request.POST or None)
    context = {
         "form":form
    }

    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = authenticate(username = username, password = password)

        if user is None:
             messages.info(request, "Kullanıcı adı veya Parola hatalı.")
             return render(request, "user/login.html", context)
        
        messages.success(request, "Başarıyla giriş yaptınız...")
        login(request, user)

        return redirect("index")
    return render(request, "user/login.html",context)

def logoutUser(request):
    logout(request)
    messages.success(request, "Başarıyla çıkış yaptınız...")
    return redirect("index")

def profileUser(request):
    user = request.user
    registration_date = user.date_joined  # Kullanıcının kayıt olduğu tarih

    context = {
        'user': user,
        'registration_date': registration_date,
    }

    return render(request, 'user/profile.html', context)
