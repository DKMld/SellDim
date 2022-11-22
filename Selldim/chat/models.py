from django.contrib.auth.models import User
from django.db import models


class ChatMessage(models.Model):
    sender = models.ForeignKey(User, related_name='messages', on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    room_name = models.CharField(max_length=100, null=True)
