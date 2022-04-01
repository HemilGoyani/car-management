from django.http import HttpResponse
from django.shortcuts import render, redirect
from car_seller.models import *
from .forms import *
from car_seller.forms import CarSellersForm
from django.db.models import Q


def home(request):
    return render(request, 'car_search.html')


def serachbox(request):
    year = request.GET.get('search')
    if year:
        shelf = CarSeller.objects.filter(Q(year__icontains=year) | Q(make__icontains=year))
        return render(request, 'search_result.html', {'shelf': shelf})  
    else:
        return HttpResponse('car not avalibale')  


def car_buyer(request, id):  
    car_id = int(id)
    car_data = CarSeller.objects.get(id = car_id)
    return render(request, 'car_buyer_form.html', {'data':car_data})


def car_buyer_save(request, id):
    car_id = int(id)
    print(request.method,"=-=-=-=-=-")
    # return HttpResponse("hello every one")
    if request.method == 'POST':
        buyer = CarBuyerForm(request.POST, request.FILES)
        print(buyer)
        if buyer.is_valid():
            buyer.save()
            return redirect('home')
        else:
            return HttpResponse('Form is not valid, please validate the form')

