from django.db import models
from django.contrib.auth.models import User


class Account(models.Model):

    def __str__(self):
        return self.username
