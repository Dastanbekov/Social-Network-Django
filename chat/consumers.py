from channels.generic.websocket import AsyncWebsocketConsumer
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from asgiref.sync import sync_to_async
from .models import Chat, Message
import json

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.chat_id = self.scope['url_route']['kwargs']['chat_id']
        self.chat_group_name = f'chat_{self.chat_id}'

        await self.channel_layer.group_add(
            self.chat_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.chat_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        data = json.loads(text_data)

        # Get data from message
        message = data['message']
        user_id = data['user_id']

        user = await sync_to_async(get_object_or_404)(User, id=user_id)
        chat = await sync_to_async(get_object_or_404)(Chat, id=self.chat_id)

        # Save message in the database
        new_message = await sync_to_async(Message.objects.create)(
            chat=chat, sender=user, content=message
        )

        await self.channel_layer.group_send(
            self.chat_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'sender': user.username,
                'timestamp': new_message.timestamp.isoformat(),
            }
        )

    async def chat_message(self, event):
        await self.send(text_data=json.dumps({
            'message': event['message'],
            'sender': event['sender'],
            'timestamp': event['timestamp'],
        }))
