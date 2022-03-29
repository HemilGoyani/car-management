from django.db import models
from django.core.validators import *
from datetime import datetime

class CarSeller(models.Model):
    POOR = 'P'
    FAIR = 'F'
    GOOD = 'G'
    EXCELLENT = 'E'
    CHOICES = (
        (POOR, "poor"),
        (FAIR, "fair"),
        (GOOD, "good"),
        (EXCELLENT,'excellent'),
    )
    year_dropdown = []
    for y in range(2011, (datetime.now().year + 5)):
        year_dropdown.append((y, y))
    seller_name = models.CharField(max_length=20)
    seller_mobile = models.CharField(max_length = 10, validators = [MinLengthValidator(10), MaxLengthValidator(10)])
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.IntegerField(('year'), max_length=4, choices=year_dropdown, default=datetime.now().year)
    Condition = models.CharField(max_length=10, choices= CHOICES)
    asking_pricce = models.FloatField(max_length=7)
    picture = models.ImageField(upload_to="media/",null=False)
    
    def __str__(self):
        return self.seller_name