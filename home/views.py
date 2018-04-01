from django.contrib.auth.forms import UserCreationForm
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
    return render(request, 'homepage.html', {})


def login_user(request):
    login_form = UserLoginForm(request.POST or None)
    if login_form.is_valid():
        username = login_form.cleaned_data.get('username')
        password = login_form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        return render(request, 'movies/movieoptions.html', {'username': username})
    return render(request, 'registration/login.html', {})


def register_user(request):
    form = UserCreationForm(request.POST)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        raw_password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=raw_password)
        login(request, user)
        return redirect('/home/login')
    return render(request, 'registration/signup.html', {'form': form})
