from django.shortcuts import render
from django.http import HttpResponse

from datetime import datetime
# Create your views here.

def index(request):
    context = {
        'year': datetime.now().year
    }

    return render(request,template_name='main/index.html',context=context)

def about(request):
    return render(request,template_name='main/about.html')