from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from django.contrib import admin
from . import views

app_name = "home"

urlpatterns = [

    # /home/
    url(r'^$', views.index, name='index'),

    # /home/login/
    url(r'^login/$', views.login_user, name='login'),

    # /home/register/
    url(r'^register/$', views.register_user, name='register'),

]
