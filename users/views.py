from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.models import User

from .forms import UserRegistrationForm
# Create your views here.

def login(request):
    return HttpResponse('login')

def logout(request):
    return HttpResponse('logout')

class UserCreationView(CreateView):
    model = User
    template_name = 'users/reg.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('main:main')