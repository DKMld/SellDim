from django.contrib.auth.models import User
from django.db import models

from Selldim.chat.managers import ChatRoomManager


class ChatMessage(models.Model):
    room_name = models.CharField(max_length=100, null=True)
    sender = models.ForeignKey(User, related_name='first_user', on_delete=models.CASCADE, null=True)
    # receiever = models.ForeignKey(User, related_name='second_user', on_delete=models.CASCADE, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)


class Messages(models.Model):
    room_name = models.ForeignKey(ChatMessage, on_delete=models.CASCADE)

    sender = models.ForeignKey(User, related_name='sender', on_delete=models.CASCADE)
    # receiever = models.ForeignKey(User, related_name='receiever', on_delete=models.CASCADE)

    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
