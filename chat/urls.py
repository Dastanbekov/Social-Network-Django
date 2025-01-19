from django.urls import path

from chat import views

app_name = 'chat'

# urlpatterns = [
#     # path('create', views.PostCreateView.as_view(), name='post-create') ,
#     # path('<slug:slug>', views.PostDetailView.as_view(),name='post'),
#     path('',views.chatlist, name='chat_list'),
#     path('user/',views.chat,name='chat')
# ]

urlpatterns = [
    path('<int:chat_id>/', views.chat_detail, name='chat_detail'),
    path('<int:chat_id>/send/', views.send_message, name='send_message'),
]