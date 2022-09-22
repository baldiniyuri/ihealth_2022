from django.db import models
from authentication.models import User


class Glucose(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    glucose = models.IntegerField()
    date_time = models.DateTimeField()