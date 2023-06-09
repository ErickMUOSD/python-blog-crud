# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(unique=True)
    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'email'
