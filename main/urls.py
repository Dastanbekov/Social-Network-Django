from django.urls import path

from main import views

urlspatterns = [
    path('',views.index)
]