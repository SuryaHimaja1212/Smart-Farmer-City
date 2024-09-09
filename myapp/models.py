from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.conf import settings 

class Product(models.Model):
    farmer=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    quantity=models.IntegerField()
    cost_per_kg=models.DecimalField(max_digits=10,decimal_places=2)
    def str  (self):
        return self.name