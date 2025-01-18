from django.urls import path

from content import views

app_name = 'content'

urlpatterns = [
    path('1', views.PostCreateView.as_view(), name='post')  #будем искать пост по слагу
]