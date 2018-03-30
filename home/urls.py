from django.conf.urls import url
from . import views

urlpatterns = [
    # /home/
    url(r'^$', views.index, name='index'),

    # /home/login/
    url(r'^login/', views.login, name='login'),

    # /home/register/
    url(r'^register/', views.register, name='register'),

]
