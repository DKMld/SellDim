from django.db import models
from django.db.models import Count


class ChatRoomManager(models.Manager):
    def get_or_create_personal_chat_room(self, user1, user2):
        chat_rooms = self.get_queryset().filter(chat_room_type='personal')
        chat_rooms = chat_rooms(user=[user1, user2]).distinct()
        chat_rooms = chat_rooms.annotate(u_count=Count('users')).filter(u_count=2)
        if chat_rooms.exists():
            return chat_rooms.first()
        else:
            chat_rooms = self.create(chat_room_type='personal')
            chat_rooms.users.add(user1)
            chat_rooms.users.add(user2)
            return chat_rooms

