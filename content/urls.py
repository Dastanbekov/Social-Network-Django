from django.urls import path

from content import views

app_name = 'content'

urlpatterns = [
    path('create', views.PostCreateView.as_view(), name='post-create') ,
    path('<slug:slug>', views.PostDetailView.as_view(),name='post'),
]