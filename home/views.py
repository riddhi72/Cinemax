from django.shortcuts import render, redirect
from .forms import Register, AccInfo, UserLoginForm
from django.contrib.auth import (
        authenticate,
        login,
        logout,
        get_user_model,
    )
from .models import Account


def index(request):
    return render(request, 'home/homepage.html', {})


def login_user(request):
    login_form = UserLoginForm(request.POST or None)
    if login_form.is_valid():
        username = login_form.cleaned_data.get('username')
        password = login_form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        return render(request, 'movies/movieoptions.html', {'username': username})
    return render(request, 'home/loginpage.html', {})


def register_user(request):
    form = Register(request.POST or None)
    acc_form = AccInfo(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        user_auth = authenticate(username=user.username, password=password)
        login(request, user_auth)
        return redirect("home/login")
    context = {"form": form, "acc_form": acc_form}
    return render(request, "home/registerpage.html", context)
