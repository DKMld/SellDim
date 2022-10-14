

from django import forms
from django.forms import ModelForm, TextInput, NumberInput, Select, ChoiceField

from Selldim.products.models import Products


class ProductForm(ModelForm):




    class Meta:
        model = Products

        category = forms.ChoiceField(required=True)
        image = forms.ImageField(required=False)

        fields = ['product_name', 'category', 'image', 'description', 'price']

        widgets = {
            'product_name': TextInput(
                attrs={
                    'class': 'product--name',
                }),

            'image': forms.FileInput(
                attrs={
                    'class': 'product--image',
                    'multiple': 'False',
                }),

            'description': forms.Textarea(
                attrs={
                    'class': 'product--description',
                    'onkeyup': "count();",
                }),

            'category': Select(attrs={
                'class': 'product--category',
                }),

            'price': NumberInput(attrs={
                'class': 'product--price',
                'min': '0',
                })

        }
