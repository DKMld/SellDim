from django.contrib.auth.models import User
from django.db import models

CATEGORY_CHOICES = [
    ('electronics', 'Electronics'),
    ('hobby', 'Hobby'),
    ('sport', 'Sport'),
    ('animals', 'Animals'),
    ('vacantions', 'Vacantions'),
    ('vehicles', 'Vehicles'),
    ('clothes', "Clothes"),
    ('tools', 'Tools'),
    ('real estate', 'Real Estate'),
    ('other', 'Other'),
]


class Products(models.Model):
    creator = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    product_name = models.CharField(max_length=100, null=True)
    description = models.TextField(null=True, max_length=1000)
    price = models.FloatField(null=True, max_length=10)
    image = models.ImageField(null=True)
    category = models.CharField(null=True, max_length=50, choices=CATEGORY_CHOICES)

