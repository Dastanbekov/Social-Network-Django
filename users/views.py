from django.shortcuts import render,redirect
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy,reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages,auth

from.utils import RedirectAuthUserMixin
from .forms import UserRegistrationForm,UserLoginForm
# Create your views here.


class UserLoginView(RedirectAuthUserMixin,LoginView):
    template_name = 'users/login.html'
    authentication_form = UserLoginForm   
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('main:main')
        return super().dispatch(request, *args, **kwargs)

class UserCreationView(RedirectAuthUserMixin,CreateView):
    model = User
    template_name = 'users/reg.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('users:login')

@login_required
def logout(request):
    messages.success(request,f'{request.user.username} - вы вышли из Аккаунта') 
    auth.logout(request)
    return redirect(reverse('main:main'))