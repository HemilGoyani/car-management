from django.db import models
from django.core.validators import *
from datetime import datetime

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
    asking_price = models.FloatField()
    picture = models.ImageField(upload_to="media/",null=False)
    is_sell = models.BooleanField(default=False)
    
    def __str__(self):
        return self.seller_name