from django.contrib.auth.models import User
from django.db import models
from django.template.defaultfilters import slugify

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

    slug = models.SlugField(null=True, unique=True)

    def __str__(self):
        return f"{self.product_name} by {self.creator}"

    def save(self, *args, **kwargs):
        super(Products, self).save(*args, **kwargs)
        if not self.slug:
            self.slug = slugify(self.category + '-' + self.product_name + '-' + str(self.id))
            self.save()




