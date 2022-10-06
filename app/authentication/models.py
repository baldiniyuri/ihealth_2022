from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    uf = models.CharField(max_length=2)
    country = models.CharField(max_length=255)
    image = models.ImageField(null=True, blank=True)
    email = models.EmailField(unique=True)
    is_pacient = models.BooleanField()
    is_medic = models.BooleanField()
    is_superuser = models.BooleanField(null=True, blank=True, default=False)

