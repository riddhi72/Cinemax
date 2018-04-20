from django.db import models


class Movie(models.Model):
    movieName = models.CharField(max_length=30)
    moviePoster = models.CharField(max_length=10000)

    def __str__(self):
        return self.movieName


class Seat(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    seatNo = models.CharField(max_length=6)
    reserved = models.BooleanField(default=False)

    def __str__(self):
        return self.seatNo
