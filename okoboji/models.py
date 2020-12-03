from django.db import models
from django.contrib.auth.admin import User
from . import admin
# Create your models here.


class Trip(models.Model):
    trip_date = models.DateField()
    attendees = models.ManyToManyField(User)
