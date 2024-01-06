from App import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('get_price/', views.get_price, name="get_price"),
    path('predict_price/', views.predict_price, name="predict_price")
]