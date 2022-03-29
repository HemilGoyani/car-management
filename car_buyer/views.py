from django.http import HttpResponse
from django.shortcuts import render, redirect
from car_seller.models import *
from .forms import *
# Create your views here.
def home(request):
    return render(request, 'car_buyer.html')

def serachbox(request):
    shelf = CarSeller.objects.filter(year=2022)
    return render(request, 'search_result.html', {'shelf': shelf})  

def car_buyer(request):
    seller = CarBuyerForm()
    if request.method == 'POST':
        if seller.is_valid():
            seller.save()
            return redirect('home')
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'car-buyer'}}">reload</a>""")
    else:
        return render(request, 'car_buyer_form.html', {'upload_form': seller})  