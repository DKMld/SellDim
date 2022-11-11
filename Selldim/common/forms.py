from django import forms


class ProductSearchForm(forms.Form):
    product_name = forms.CharField(
        max_length=50,
        required=False,
    )