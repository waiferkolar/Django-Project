from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    name = models.CharField(max_length=100)
    image = models.CharField(max_length=225)
    price = models.IntegerField()
    description = models.TextField()
    author = models.ForeignKey(User,on_delete=models.CASCADE)


