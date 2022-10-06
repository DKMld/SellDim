
from django.db import models
from django import forms


class Accounts(models.Model):
    username = models.CharField(max_length=30, null=False, blank=False)
    password = models.CharField(max_length=30, blank=False, null=False)
    image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100, blank=True)


