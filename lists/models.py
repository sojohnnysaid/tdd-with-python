from django.db import models
from django.db.models.deletion import CASCADE
from django.core.validators import MinLengthValidator

# Create your models here.

class List(models.Model):
    text = models.TextField(default='')

class Item(models.Model):
    text = models.TextField(validators=[MinLengthValidator(1, message='You can\'t  have an empty list item')])
    list = models.ForeignKey(List, default=None, on_delete=CASCADE)