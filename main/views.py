from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

from datetime import datetime

from .utils import NavbarMixin
# Create your views here.

class IndexView(NavbarMixin,TemplateView):
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['year'] = datetime.now().year
        # context['menu'] = self.get_navbar_context() #getting navbar context from .utils 
        return context

class AboutView(NavbarMixin,TemplateView):
    template_name ='main/about.html'