from django.shortcuts import render
from car_seller.models import *
# Create your views here.
def home(request):
    return render(request, 'car_buyer.html')

def serachbox(request):
    # print(request.GET['search'])
    shelf = CarSeller.objects.filter(year=2022)
    return render(request, 'search_result.html', {'shelf': shelf})  