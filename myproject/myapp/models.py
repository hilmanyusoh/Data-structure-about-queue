from django.db import models

# Create your models here.

class Queue(models.Model):
    name = models.CharField(max_length=100)
    order = models.CharField(max_length=100)