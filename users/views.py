from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def login(request):
    return HttpResponse('login')

def logout(request):
    return HttpResponse('logout')

def register(request):
    return HttpResponse('register')