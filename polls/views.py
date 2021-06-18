from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    return HttpResponse("Hello, world. This is from Pycharm IDE.")

def owner(request):
       return HttpResponse("Hello, world. d72eecc6 is the polls index.")