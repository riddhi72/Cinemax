from django.db import models


class Account(models.Model):
    username = models.CharField(max_length=15)
    password = models.CharField(max_length=15)

    def __str__(self):
        return self.username
