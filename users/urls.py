from django.urls import path

from users import views

app_name = 'users'

urlpatterns = [
    path('login/',views.UserLoginView.as_view() , name='login'),
    path('register/',views.UserCreationView.as_view(),name='register'),
    path('profile/<str:username>',views.UserProfileView.as_view(),name='profile'),
    path('follow/<str:username>/', views.follow_user, name='follow_user'),
    path('unfollow/<str:username>/', views.unfollow_user, name='unfollow_user'),
    path('logout/',views.logout, name='logout'),
]