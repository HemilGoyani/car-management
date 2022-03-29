from django.http import HttpResponse
from car_seller.models import *
from .forms import *
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib import messages


def index(request):
    shelf = CarSeller.objects.all()
    return render(request, 'index.html', {'shelf': shelf})


def login_user(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username = cd['username'],
                                password = cd['password'])
            if user is not None:
                login(request, user)
                return HttpResponse('Authentication was successfull')
            else:
                return HttpResponse("Invalid username or password.")
        
    form = LoginForm()
    return render(request, "login.html", {'form':form})

def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("main:homepage")
        messages.error(
            request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request=request, template_name="register.html", context={"register_form": form})
