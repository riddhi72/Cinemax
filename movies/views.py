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
    if request.user.is_authenticated:
        return render(request, 'movies/movieselected.html', {'movie': movie})
    else:
        raise Http404("Please Log In To Access the Site.")


def reserved_seats(request, smovie):
    movie = get_object_or_404(Movie, pk=smovie)
    context = {
        'movie': movie,
        'error_message': "You Did Not Select Any Seats",
    }
    if request.user.is_authenticated:
        try:
            booked_seats = request.POST.getlist('reserved_seats')
        except (KeyError, Seat.DoesNotExist):
            return render(request, 'movies/movieselected.html', context)
        else:
            for a in booked_seats:
                m1 = Seat.objects.get(pk=a)
                m1.reserved = True
                m1.save()
            count = len(booked_seats)
            total = count*150
            return render(request, 'movies/moviepayment.html', {'movie': movie, 'total': total})
    else:
        raise Http404("Please Log In To Access the Site.")


def payment(request, smovie):
    movie = get_object_or_404(Movie, pk=smovie)
    if request.user.is_authenticated:
        return render(request, 'movies/moviepayment.html', {'movie': movie})
    else:
        raise Http404("Please Log In To Access the Site.")
