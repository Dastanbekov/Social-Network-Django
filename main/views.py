from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from django.views.generic.list import ListView

from datetime import datetime

from content.models import Post
from .utils import NavbarMixin
# Create your views here.

from django.views.generic import TemplateView
from django.core.paginator import Paginator
from content.models import Post
from django.contrib.auth.models import User
from datetime import datetime

class IndexView(NavbarMixin, TemplateView):
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['year'] = datetime.now().year
        context['users'] = User.objects.all()

        posts = Post.objects.filter(is_published=True).order_by('-created_at')
        
        # pagination
        paginator = Paginator(posts, 5)
        page_number = self.request.GET.get('page') 
        page_obj = paginator.get_page(page_number)  

        context['posts'] = page_obj  
        context['page_obj'] = page_obj  
        return context