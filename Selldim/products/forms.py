from django import forms
from django.forms import ModelForm, TextInput, NumberInput, Select
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
                    'placeholder': 'Example: Apple Iphone 14pro 256gb',
                }),

            'image': forms.FileInput(
                attrs={
                    'class': 'product--image',
                    'multiple': 'False',
                    'onchange': 'readURL(this);'
                }),


            'description': forms.Textarea(
                attrs={
                    'class': 'product--description',
                    'onkeyup': "count();",
                    'placeholder': 'Write something that you think will convince someone to buy your product'
                }),

            'category': Select(attrs={
                'class': 'product--category',
                }),

            'price': NumberInput(attrs={
                'class': 'product--price',
                'min': '0',
                })
        }


class EditProductForm(ProductForm):
    pass


class DeleteProductForm(ProductForm):
    pass
