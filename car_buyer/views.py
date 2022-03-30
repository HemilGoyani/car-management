from django.http import HttpResponse
from django.shortcuts import render, redirect
from car_seller.models import *
from .forms import *
from car_seller.forms import CarSellersForm



def home(request):
    return render(request, 'car_search.html')


def serachbox(request):
    year = request.GET.get('search')
    shelf = CarSeller.objects.filter(year=year)
    return render(request, 'search_result.html', {'shelf': shelf})  


def car_buyer(request):  
    buyer = CarBuyerForm()
    if request.method == 'POST':
        buyer = CarBuyerForm(request.POST, request.FILES)
        if buyer.is_valid():
            buyer.save()
            return redirect('home')
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'home'}}">reload</a>""")
    else:
        return render(request, 'car_buyer_form.html', {'upload_form': buyer})

    
