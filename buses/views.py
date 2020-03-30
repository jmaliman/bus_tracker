from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, StreamingHttpResponse
from .models import *
import time
import webbrowser
# Create your views here.


def index(request):
    return render(request, 'buses/index.html', {})

def generate_buses(request):
    buses=get_buses()

    return render(request, 'buses/busgenerator.html', {'buses': buses})

