from django.db import models
from django.contrib.auth.models import User
from Selldim.products.models import Products


class ProductLikes(models.Model):
    product = models.ForeignKey(Products, on_delete=models.RESTRICT, null=False, blank=False)
    user = models.ForeignKey(User, on_delete=models.RESTRICT)

    def __str__(self):
        return f"{self.product} liked by {self.user}"
