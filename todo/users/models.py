from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class Users(AbstractUser):
    photo = models.ImageField(upload_to='users_images', blank=True)
    age = models.PositiveIntegerField(default=18)
    email = models.EmailField(max_length=128, unique=True)

    def __str__(self):
        return self.username
