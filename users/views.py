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
from .utils import AnonymousOnlyMixin
# Create your views here.


class UserLoginView(AnonymousOnlyMixin,NavbarMixin,LoginView):
    template_name = 'users/login.html'
    authentication_form = UserLoginForm   

class UserCreationView(AnonymousOnlyMixin,NavbarMixin,CreateView):
    model = User
    template_name = 'users/reg.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('users:login')

class UserProfileView(NavbarMixin,DetailView):
    template_name = 'users/profile.html'
    model = User

    #берем юзернейм из адреснной строки
    def get_object(self):
        username = self.kwargs.get('username')  
        user = get_object_or_404(User, username=username)
        return user

    #определяем шаблон для пользователя
    def get_template_names(self):
        user = self.get_object()
        if self.request.user == user:
            return ['users/my_profile.html'] 
        else:
            return ['users/profile.html'] 

@login_required
def logout(request):
    messages.success(request,f'{request.user.username} - вы вышли из Аккаунта') 
    auth.logout(request)
    return redirect(reverse('main:main'))