from tkinter.tix import Form
from django import forms
from .models import *


class CarBuyerForm(forms.Form):
    buyer_name = forms.CharField(max_length=20)
    buyer_mobile = forms.CharField(max_length=10)
    make = forms.CharField(max_length=50)
    model = forms.CharField(max_length=50)
    year = forms.IntegerField()
    Condition = forms.CharField(max_length=10)
    asking_pricce = forms.FloatField()
    # class Meta:
    #     model = CarBuyer
    #     fields = '__all__'
