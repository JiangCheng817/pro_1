from django.db import models


# Create your models here.
class Book(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField(max_length=10)
    price = models.TextField(max_length=10)


# class person(models.Model):
#     id = models.IntegerField(primary_key=True)
#     name = models.TextField(max_length=10)
#     price = models.TextField(max_length=10)