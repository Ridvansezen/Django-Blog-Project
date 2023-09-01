from django.shortcuts import render

def registerUser(request):
    return render(request, "user/register.html")

def loginUser(request):
    return render(request, "user/login.html")

def logoutUser(request):
    pass
