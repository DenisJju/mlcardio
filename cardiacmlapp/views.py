from django.http import HttpResponse httpResponseNotFound
from django.urls import path, include
from django.conf.urls import handler404
from django.shortcuts import render

def handle404(request, exception):
    return HttpResponse("Page not found", status=404)

def index(request):
    return HttpResponse("Welcome to the Cardiac ML App! This is the home page.")

