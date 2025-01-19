from django.shortcuts import render
# Create your views here.

from .models import Chat
from django.views.generic import ListView, DetailView

from main.utils import NavbarMixin
# Views for chat application

class ChatListView(NavbarMixin,ListView):
    model = Chat
    template_name = 'chat/chat_list.html'
    context_object_name = 'chats'

    def get_queryset(self):
        return self.request.user.chats.all()

class ChatDetailView(NavbarMixin,DetailView):
    model = Chat
    template_name = 'chat/chat_detail.html'
    context_object_name = 'chat'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['messages'] = self.object.messages.order_by('timestamp')
        return context