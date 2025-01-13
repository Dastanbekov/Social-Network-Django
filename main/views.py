from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse('Hello!')

def about_us(request):
    return HttpResponse('About us')

