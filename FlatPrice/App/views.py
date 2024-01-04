from django.shortcuts import render
from model import modelLoader


model = modelLoader.Model()

def home(request):
    price = model.get_data([[44, 28, 6.0, 23.5, 7, 1, 0, 1]])
    return render(request, 'App/home.html', {"price": price})

def get_data(request):
    price = model.get_data([[44, 28, 6.0, 16.5, 7, 1, 0, 1]])
    return render(request, 'App/price.html', {"price": price})
