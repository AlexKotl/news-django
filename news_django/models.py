from django.contrib.auth.models import AbstractUser, User
from django.db import models

class MyUser(AbstractUser):
    birthday = models.DateField(blank=True)
    email = models.CharField(max_length=180, unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []