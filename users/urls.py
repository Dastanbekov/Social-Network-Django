from django.urls import path

from users import views

app_name = 'users'

urlpatterns = [
    path('login/',views.UserLoginView.as_view() , name='login'),
    path('logout/',views.logout, name='logout'),
    path('register/',views.UserCreationView.as_view(),name='register'),
    path('profile/',views.UserProfileView.as_view(),name='profile'),
]