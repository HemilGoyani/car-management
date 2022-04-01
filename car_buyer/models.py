from django.db import models
from django.core.validators import *


class CarBuyer(models.Model):
    buyer_name = models.CharField(max_length=20)
    buyer_mobile = models.CharField(max_length = 10, validators = [MinLengthValidator(10), MaxLengthValidator(10)])
    email = models.EmailField()
    make = models.CharField(max_length=50,null=True, blank=True)
    model = models.CharField(max_length=50,null=True, blank=True)
    year = models.IntegerField(null=True, blank=True)
    Condition = models.CharField(max_length=10,null=True, blank=True)
    asking_price= models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return self.buyer_name