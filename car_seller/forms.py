from dataclasses import field, fields
from tkinter.tix import Form
from django import forms
from .models import *


class CarSellersForm(forms.ModelForm):
    class Meta:
        model = CarSeller
        fields = ['seller_name', 'seller_mobile', 'email', 'make', 'model','year', 'Condition', 'asking_price', 'picture']
        # fields = '__all__'
