from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
# Create your views here.

from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from .models import Chat,Message

@login_required
def chat_detail(request, chat_id):
    chat = get_object_or_404(Chat, id=chat_id, participants=request.user)
    messages = chat.messages.order_by('timestamp')
    return render(request, 'chat/chat_detail.html', {'chat': chat, 'messages': messages})

@login_required
def send_message(request, chat_id):
    if request.method == "POST":
        chat = get_object_or_404(Chat, id=chat_id, participants=request.user)
        content = request.POST.get("content")
        if content:
            message = Message.objects.create(chat=chat, sender=request.user, content=content)
            return JsonResponse({"status": "success", "message": message.content, "timestamp": message.timestamp})
    return JsonResponse({"status": "error", "message": "Invalid request"})