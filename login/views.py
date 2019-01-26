from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# Create your views here.


def get_login(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == "POST":
            user = request.POST.get('user')
            password = request.POST.get('pass')
            auth = authenticate(request, username=user, password=password)
            if auth is not None:
                login(request, auth)
                messages.add_message(request, messages.INFO, 'Login successfully complete')
                return redirect('index')

    return render(request, "login.html")


"""
This Function Work
"""


def get_logout(request):
    logout(request)
    return redirect('index')
