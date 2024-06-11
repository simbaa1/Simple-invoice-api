from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    name = models.CharField(blank=True, max_length=200)

    def __str__(self):
        return self.email


