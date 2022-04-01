from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import *
from .forms import CarSellersForm
from django.core.paginator import Paginator
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def home(request):
    user_list = CarSeller.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(user_list,4)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)

    return render(request, 'home.html', { 'users': users })

def seller(request):
    seller = CarSellersForm()
    if request.method == 'POST':
        seller = CarSellersForm(request.POST, request.FILES)
        if seller.is_valid():
            print()
            seller.save()
            return redirect('success')
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'home'}}">reload</a>""")
    else:
        return render(request, 'car_seller.html', {'upload_form': seller})
    
    
def update_car(request, car_id):
    car_id = int(car_id)
    try:
        car = CarSeller.objects.get(id=car_id)
    except CarSeller.DoesNotExist:
        return redirect('home')
    car_form = CarSellersForm(request.POST or None, instance=car)
    if car_form.is_valid():
        car_form.save()
        return redirect('home')
    return render(request, 'car_seller.html', {'upload_form': car_form})


def delete_car(request, car_id):
    car_id = int(car_id)
    try:
        book_sel = CarSeller.objects.get(id=car_id)
    except CarSeller.DoesNotExist:
        return redirect('home')
    book_sel.delete()
    return redirect('home')


def successform(request):
    return render(request, 'success.html')
