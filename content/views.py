from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from .models import Post
from .forms import PostForm
from main.utils import NavbarMixin
# Create your views here.

class PostCreateView(NavbarMixin,CreateView):
    model = Post
    template_name = 'content/post_form.html'
    form_class = PostForm
    success_url = reverse_lazy('main:main')

    def form_valid(self, form):
        form.instance.author = self.request.user    
        return super().form_valid(form)
    