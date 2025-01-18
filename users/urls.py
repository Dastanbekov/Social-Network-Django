from django.urls import path

from users import views

app_name = 'users'

urlpatterns = [
    path('login/',views.UserLoginView.as_view() , name='login'),
    path('register/',views.UserCreationView.as_view(),name='register'),
    path('profile/<str:username>',views.UserProfileView.as_view(),name='profile'),
    path('logout/',views.logout, name='logout'),
]