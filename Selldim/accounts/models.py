from django.contrib.auth.models import User
from django.db import models


class ProfilePicture(models.Model):
    user = models.ForeignKey(User, on_delete=models.RESTRICT, null=True)
    user_picture = models.ImageField(null=True)

    def __str__(self):
        return f"{self.user}: {self.user_picture}"


class UserComments(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment_sender')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment_receiever')
    comment = models.TextField(max_length=200)

    def __str__(self):
        return f"{self.user}: {self.comment}"

