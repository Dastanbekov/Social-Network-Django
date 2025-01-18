from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy,reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages,auth
from django.http import Http404

from django.views.generic import DetailView

from .forms import UserRegistrationForm,UserLoginForm
from main.utils import NavbarMixin
from .utils import AnonymousOnlyMixin, FollowMixin
from .models import Follow
# Create your views here.


class UserLoginView(AnonymousOnlyMixin,NavbarMixin,LoginView):
    template_name = 'users/login.html'
    authentication_form = UserLoginForm   

class UserCreationView(AnonymousOnlyMixin,NavbarMixin,CreateView):
    model = User
    template_name = 'users/reg.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('users:login')

class UserProfileView(FollowMixin,NavbarMixin,DetailView):
    template_name = 'users/profile.html'
    model = User

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        
        # Получаем количество подписчиков и подписок
        context['followers_count'] = self.get_followers_count(user)
        context['following_count'] = self.get_following_count(user)
        context['is_following'] = self.is_following(self.request.user, user)
        
        return context

@login_required
def follow_user(request, username):
    followed_user = get_object_or_404(User, username=username)
    if followed_user == request.user:
        raise Http404("You can't follow yourself.")

    # Если пользователь еще не подписан
    if not Follow.objects.filter(user=request.user, followed_user=followed_user).exists():
        Follow.objects.create(user=request.user, followed_user=followed_user)
    
    return redirect('users:profile', username=username)


@login_required
def unfollow_user(request, username):
    followed_user = get_object_or_404(User, username=username)
    if followed_user == request.user:
        raise Http404("You can't unfollow yourself.")

    # Если подписка существует, удаляем ее
    Follow.objects.filter(user=request.user, followed_user=followed_user).delete()
    
    return redirect('users:profile', username=username)


@login_required
def logout(request):
    messages.success(request,f'{request.user.username} - вы вышли из Аккаунта') 
    auth.logout(request)
    return redirect(reverse('main:main'))