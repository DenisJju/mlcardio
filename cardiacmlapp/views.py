from django.http import HttpResponse, HttpResponseNotFound

from django.urls import path, include
from django.conf.urls import handler404
from django.shortcuts import render

def handle404(request, exception):
    return HttpResponse("Page not found", status=404)

# def index(request):
#     #return HttpResponse(request, 'cardiacmlapp/index.html')
#     form = YourForm()
#     return render(request, 'predictor/index.html', {'form': form})

from predictor.forms import InputForm

def index(request):
    form = InputForm()
    return render(request, 'predictor/index.html', {'form': form})
