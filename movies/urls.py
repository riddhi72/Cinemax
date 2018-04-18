from django.conf.urls import url
from . import views

app_name = 'movies'

urlpatterns = [

    # /movies/
    url(r'^$', views.all_movies, name='allMovies'),

    # /movies/selected_movie
    url(r'^(?P<smovie>[0-9]+)$', views.selected_movie, name='selected_Movie'),

    # /movies/selected_movie/reserved/
    url(r'^(?P<smovie>[0-9]+)/reserved/$', views.reserved_seats, name='reserved_seats'),

    # /movies/selected_movie/payment/
    url(r'^(?P<smovie>[0-9]+)/payment/$', views.payment, name='payment'),
]
