from django.shortcuts import render
from django.http import HttpResponseRedirect
from model import modelLoader

from .forms import Price
from .models import Price as PriceModel


model = modelLoader.Model()

def home(request):

    return render(request, 'App/home.html')

def get_price(request):
    if request.method == "POST":
        form = Price(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return HttpResponseRedirect("/predict_price")
    else:
        form = Price()

    return render(request, "App/price.html", {"form": form})

def predict_price(request):
    # price = model.get_data([[44, 28, 6.0, 16.5, 7, 1, 0, 1]])
    price = PriceModel.objects.last()
    predict_price = [[
        price.totsp,
        price.livesp,
        price.kitsp,
        price.dist,
        price.metrdist,
        1 if price.walk == True else 0,
        1 if price.brick == True else 0,
        1 if price.floor == True else 0
    ]]
    predict_price = round(float(model.get_predict(predict_price)[0]) * 100_000, 2)
    return render(request, 'App/predict.html', {"price": predict_price})