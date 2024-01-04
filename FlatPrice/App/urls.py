from App import views
from django.urls import path

urlpatterns = [
    path('', views.home),
    path('get_data', views.get_data)
]