from django.db import models
from django.core.validators import *
from datetime import datetime
from djmoney.models.fields import MoneyField
from djmoney.money import Money
from djmoney.models.validators import MaxMoneyValidator, MinMoneyValidator
from djmoney.models.managers import money_manager


class CarSeller(models.Model):
    POOR = 'Poor'
    FAIR = 'Fair'
    GOOD = 'Good'
    EXCELLENT = 'Eexcellent'
    CHOICES = (
        (POOR, "poor"),
        (FAIR, "fair"),
        (GOOD, "good"),
        (EXCELLENT,'excellent'),
    )
    year_dropdown = []
    for y in range(2011, (datetime.now().year + 1)):
        year_dropdown.append((y, y))
    seller_name = models.CharField(max_length=20)
    seller_mobile = models.CharField(max_length = 10, validators = [MinLengthValidator(10), MaxLengthValidator(10)])
    email = models.EmailField(null=True )
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.IntegerField(('year'),choices=year_dropdown, default=datetime.now().year)
    Condition = models.CharField(max_length=10, choices= CHOICES)
    asking_price= MoneyField(max_digits=8,
        decimal_places=2,validators=[MinMoneyValidator(1000),
        MaxMoneyValidator(100000),] ,default_currency='USD')
    picture = models.ImageField(upload_to="media/",null=False)
    is_sell = models.BooleanField(default=False)
    
    def __str__(self):
        return self.seller_name