from django.db import models
from authentication.models import User


class Historic(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    historic = models.TextField()
    medicines = models.TextField(null=True)
    surgeries = models.TextField(null=True)