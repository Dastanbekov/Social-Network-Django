from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy,reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages,auth

from django.views.generic import DetailView

from .forms import UserRegistrationForm,UserLoginForm
from main.utils import NavbarMixin
# Create your views here.


class UserLoginView(NavbarMixin,LoginView):
    template_name = 'users/login.html'
    authentication_form = UserLoginForm   

class UserCreationView(NavbarMixin,CreateView):
    model = User
    template_name = 'users/reg.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('users:login')

class UserProfileView(NavbarMixin,DetailView):
    template_name = 'users/profile.html'
    model = User
    def get_object(self):
        return get_object_or_404(User,pk = self.request.user.pk)


@login_required
def logout(request):
    messages.success(request,f'{request.user.username} - вы вышли из Аккаунта') 
    auth.logout(request)
    return redirect(reverse('main:main'))