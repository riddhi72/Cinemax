from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.contrib import admin
from . import views

urlpatterns = [

    url(r'^admin/', admin.site.urls),

    # /home/
    url(r'^$', views.index, name='index'),

    # /home/login/
    url(r'^login/$', auth_views.login, name='login'),

    # /home/register/
    url(r'^register/$', views.register_user, name='register'),

    # /home/
    url(r'^logout/$', auth_views.logout, {'next_page': '/login'}, name='logout'),
]
