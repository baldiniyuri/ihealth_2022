from django.db import models
from authentication.models import User


class Glucose(models.Model):
    glucose = models.IntegerField()
    date_time = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)