from django.shortcuts import render
from django.conf import settings
from .model import modelLoader

def home(request):
    price = modelLoader.get_data()
    return render(request, 'App/home.html', {"price": price})
