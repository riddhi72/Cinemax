from django.conf.urls import url
from . import views

urlpatterns = [

    # /movies/
    url(r'^$', views.all_movies, name='allMovies'),

    # /movies/selected_movie
    url(r'^(?P<smovie>[0-9]+)$', views.selected_movie, name='selected_Movie'),
]
