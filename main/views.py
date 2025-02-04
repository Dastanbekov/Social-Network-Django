from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from django.views.generic.list import ListView

from datetime import datetime

from content.models import Post
from .utils import NavbarMixin
# Create your views here.


## YBIRAEM MAIN>PAGE
class IndexView(NavbarMixin,TemplateView):
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['year'] = datetime.now().year
        context['users'] = User.objects.all()
        context['posts'] = Post.objects.all()
        return context
    