from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.

class List(models.Model):
    text = models.TextField(default='')

class Item(models.Model):
    text = models.TextField(default='')
    list = models.ForeignKey(List, default=None, on_delete=CASCADE)