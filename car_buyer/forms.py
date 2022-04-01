from tkinter.tix import Form
from django import forms
from .models import *


class CarBuyerForm(forms.Form):
    
    class Meta:
        model = CarBuyer
        fields = '__all__'
