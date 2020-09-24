from django.db import models

# Create your models here.


class User(models.Model):
    Name = models.CharField(max_length=20)
    Status = models.CharField(max_length=500)
    Size = models.FloatField()
    Latitude = models.FloatField()
    Longitude = models.FloatField()