from django.shortcuts import render, get_object_or_404
from .models import Movie


def all_movies(request):
    movielist = Movie.objects.all()
    context = {'movielist': movielist, }
    return render(request, 'movies/movieoptions.html', context)


def selected_movie(request, smovie):
    movie = get_object_or_404(Movie, pk=smovie)
    context = {
        'movie': movie,
        'smovie': smovie,
    }
    return render(request, 'movies/movieselected.html', context)
