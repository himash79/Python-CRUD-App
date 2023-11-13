from django.db import models
from rest_framework import serializers


# Create your models here.
class User(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    image = models.ImageField(upload_to='pics')
    status = models.BooleanField(default=False)