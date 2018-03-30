from django.shortcuts import render, get_object_or_404
from .models import Movie
from home.models import Account


def all_movies(request, user_id):
    user = get_object_or_404(Account, pk=user_id)
    movielist = Movie.objects.all()
    context = {
        'user': user,
        'movielist': movielist,
        'user_id': user_id,
    }
    return render(request, 'movies/movieoptions.html', context)


def selected_movie(request, user_id, smovie):
    user = get_object_or_404(Account, pk=user_id)
    movie = get_object_or_404(Movie, pk=smovie)
    context = {
        'user': user,
        'movie': movie,
        'user_id': user_id,
        'smovie': smovie,
    }
    return render(request, 'movies/movieselected.html', context)
