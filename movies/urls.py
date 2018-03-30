from django.conf.urls import url
from . import views

urlpatterns = [

    # /movies/user_id/
    url(r'^(?P<user_id>[0-9]+)$', views.all_movies, name='allMovies'),

    # /movies/user_id/selected_movie
    url(r'^(?P<user_id>[0-9])+/(?P<smovie>[0-9]+)$', views.selected_movie, name='selected_Movie'),
]
