from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("<h1>Hello there!</h1>")

def products(request):
    prod_list=['iPhone','iPad','iMac']
    return HttpResponse('<h1>%s</h1>'%i for i in prod_list)
