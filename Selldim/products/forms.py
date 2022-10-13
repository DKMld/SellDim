
from django import forms
from django.forms import ModelForm, TextInput, FileField, ImageField

from Selldim.products.models import Products


class ProductForm(ModelForm):
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

    file = forms.ImageField(required=False,)
    category = forms.ChoiceField(required=True, choices=CATEGORY_CHOICES)

    class Meta:
        model = Products

        fields = ['product_name', 'image', 'description', 'price']

        widgets = {
            'product_name': TextInput(
                attrs={
                    'class': 'product--name'}),

            'image': forms.FileInput(
                attrs={
                    'class': 'product--image'}),

            'description': TextInput(
                attrs={
                    'class': 'product--description'}),

        }
