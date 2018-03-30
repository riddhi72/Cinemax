from django.db import models


class Movie(models.Model):
    movieName = models.CharField(max_length=15)
    moviePoster = models.CharField(max_length=1000)

    def __str__(self):
        return self.movieName
