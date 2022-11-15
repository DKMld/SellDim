from django.contrib.auth.models import User
from django.db import models


class ProfilePicture(models.Model):
    user = models.ForeignKey(User, on_delete=models.RESTRICT, null=True)
    user_picture = models.ImageField(null=True)
