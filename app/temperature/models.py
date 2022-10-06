from django.db import models
from authentication.models import User


class Temperature(models.Model):
    temperature = models.FloatField()
    date_time = models.DateTimeField(auto_now_add=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)