from django.db import models
from django.db.models.fields import DateTimeField
from authentication.models import User


class BloodPressue(models.Model):
    systolic_level = models.IntegerField()
    diastolic_level = models.IntegerField()
    bpm = models.IntegerField()
    date_time = DateTimeField(auto_now_add=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)