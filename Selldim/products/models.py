from django.contrib.auth.models import User
from django.db import models


class Products(models.Model):
    creator = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    product_name = models.CharField(max_length=100, null=True)
    description = models.TextField(null=True, max_length=300)
    price = models.FloatField(null=True, max_length=10)
    image = models.ImageField(null=True)
    category = models.CharField(null=True, max_length=50)

