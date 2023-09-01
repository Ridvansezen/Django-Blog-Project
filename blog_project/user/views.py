from django.shortcuts import render
from .forms import RegisterForm

def registerUser(request):

    form = RegisterForm()
    context = {
        "form": form,
    }

    return render(request, "user/register.html", context)

def loginUser(request):
    return render(request, "user/login.html")

def logoutUser(request):
    pass
