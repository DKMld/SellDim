from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class ChatMessage(models.Model):
    sender = models.ForeignKey(User, related_name='messages', on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)