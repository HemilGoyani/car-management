from django.db import models
from django.core.validators import *
from datetime import datetime
from django.contrib.auth.models import User

class CarBuyer(models.Model):
    
    buyer_name = models.CharField(max_length=20)
    buyer_mobile = models.CharField(max_length=10, validators=[
                                    MinLengthValidator(10), MaxLengthValidator(10)])
    make = models.CharField(max_length=50, null=True)
    model = models.CharField(max_length=50, null=True)
    year = models.IntegerField(default=2022)
    Condition = models.CharField(max_length=10, default='Good')
    asking_pricce = models.FloatField(default=15000)    
    # user_id = models.ForeignKey(User,on_delete=models.CASCADE,editable=False,null=True,blank=True)