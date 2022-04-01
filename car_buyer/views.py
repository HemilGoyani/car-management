from django.http import HttpResponse
from django.shortcuts import render, redirect
from car_seller.models import *
from .forms import *
from django.db.models import Q
from car_seller.models import CarSeller


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
        buyer_save = CarBuyerForm(request.POST, request.FILES)
        if buyer_save.is_valid():
            print("method is valid=-=-=-=-=-")
            name = request.POST.get('buyer_name')
            number = request.POST.get('buyer_mobile')
            email = request.POST.get('email')
            make = request.POST.get('make')
            model = request.POST.get('model')
            year = request.POST.get('year')            
            condition = request.POST.get('condition')  
            asking_price = request.POST.get('asking_price')
            print(asking_price)
            buyer_data = CarBuyer(buyer_name=name, buyer_mobile=number, email=email, make=make, model=model, year=year, Condition=condition, asking_price=asking_price)
            buyer_data.save()
            car_sold = CarSeller.objects.get(id = car_id)
            car_sold.is_sell = True
            car_sold.save()
            return redirect('home')
        
        else:
            return HttpResponse('Form is not valid, please validate the form')

