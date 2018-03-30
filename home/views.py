from django.shortcuts import render
'''
from django.shortcuts import render, redirect
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,
)
from .forms import UserLoginForm, UserRegisterForm'''


def index(request):
    context = {}
    return render(request, 'home/homepage.html', context)


def login(request):
    context = {}
    return render(request, 'home/loginpage.html', context)
    '''
    print(request.user.is_authenticated())
    title = "Login"
    userLogin = UserLoginForm(request.POST or None)
    if userLogin.is_valid():
        username = userLogin.cleaned_data.get("username")
        password = userLogin.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        userLogin(request, user)
        return redirect("/")

    return render(request, "login.html", {"login": login, "title": title})
    '''


def register(request):
    context = {}
    return render(request, 'home/registerpage.html', context)
