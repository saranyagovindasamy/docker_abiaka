from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. This is the demo to create the pipline for the automation.")

def about(request):
    return HttpResponse("This is about page")

def abiaka(request):
    return HttpResponse("This is abiaka page")