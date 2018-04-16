from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Movie, Seat


def all_movies(request):
    movielist = Movie.objects.all()
    context = {'movielist': movielist, }
    if request.user.is_authenticated:
        return render(request, 'movies/movieoptions.html', context)
    else:
        raise Http404("Please Log In To Access the Site.")


def selected_movie(request, smovie):
    movie = get_object_or_404(Movie, pk=smovie)
    seats = Seat.objects.filter(movie=smovie)
    context = {
        'movie': movie,
        'smovie': smovie,
        'seats': seats,
    }
    if request.user.is_authenticated:
        return render(request, 'movies/movieselected.html', context)
    else:
        raise Http404("Please Log In To Access the Site.")
