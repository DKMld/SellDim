
from django import forms
from django.forms import Form, ModelForm

from Selldim.products.models import Products


class ProductForm(ModelForm):
    image = forms.ImageField(required=False)

    class Meta:
        model = Products

        fields = ['product_name', 'image', 'description', 'price']



