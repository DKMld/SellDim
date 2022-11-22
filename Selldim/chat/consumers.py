import json

from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer
from django.contrib.auth.models import User

from Selldim.chat.models import ChatMessage


class ChatRoomConsumer(AsyncWebsocketConsumer):
    @database_sync_to_async
    def create_chat(self, message, sender, room_name):

        return ChatMessage.objects.create(sender=sender, message=message, room_name=room_name)

    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name,
        )

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name,
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        user_username = text_data_json['user_username']

        room_name = text_data_json['room_name']

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chatroom_message',
                'message': message,
                'user_username': user_username,

                'room_name': room_name,
            }
        )

    async def chatroom_message(self, event):
        message = event['message']
        user_username = event['user_username']
        user = await database_sync_to_async(User.objects.get)(username=event['user_username'])
        room_name = event['room_name']

        new_messages = await self.create_chat(message=message, sender=user, room_name=room_name)

        await self.send(text_data=json.dumps({
            'message': message,
            'user_username': user_username,

        }))