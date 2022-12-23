import json
from asgiref.sync import sync_to_async
from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer
from django.contrib.auth.models import User
from Selldim.chat.models import ChatMessage, Messages


class ChatRoomConsumer(AsyncWebsocketConsumer):
    @database_sync_to_async
    def create_chat(self, room_name, sender, username):
        user_list = [sender, username]
        if ChatMessage.objects.filter(room_name=room_name, sender__in=user_list, receiever__in=user_list):
            return ChatMessage.objects.filter(room_name=room_name, sender__in=user_list, receiever__in=user_list).get()
        return ChatMessage.objects.get_or_create(room_name=room_name, sender=sender, receiever=username)

    @database_sync_to_async
    def create_message(self, room_name, sender, username, message):
        user_list = [sender, username]
        return Messages.objects.create(room_name=room_name, sender=sender, receiever=username, message=message)

    @sync_to_async
    def get_current_chat_room(self, room_name, sender, username):
        user_list = [sender, username]
        return ChatMessage.objects.filter(room_name=room_name, sender__in=user_list, receiever__in=user_list).get()

    async def connect(self):

        self.username = self.scope['url_route']['kwargs']['username']
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name
        self.me = self.scope['user'].username

        self.other_user_username = self.scope['url_route']['kwargs']['username']
        self.other_user = User.objects.filter(username=self.other_user_username)
        # print(self.other_user)
        # self.other_user = user object

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
        username = self.username

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chatroom_message',
                'message': message,
                'user_username': user_username,
                'room_name': room_name,
                'username': username,
            }
        )

    async def chatroom_message(self, event):
        message = event['message']
        user_username = event['user_username']
        username = self.username
        # print(username)
        room_name = event['room_name']

        user = await database_sync_to_async(User.objects.get)(username=event['user_username'])
        receiever = await database_sync_to_async(User.objects.get)(username=event['username'])

        new_chat_room = await self.create_chat(room_name=room_name, sender=user, username=receiever)

        current_chat_room = await self.get_current_chat_room(room_name=room_name, sender=user, username=receiever)

        new_message = await self.create_message(
            room_name=current_chat_room, sender=user, message=message, username=receiever)

        await self.send(text_data=json.dumps({
            'message': message,
            'user_username': user_username,
            'username': username,
        }))
