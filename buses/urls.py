from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name = 'index'),
    path('bus_generator',views.generate_buses, name = 'generate_buses'),
]
