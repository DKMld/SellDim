from django import forms

from Selldim.accounts.models import Accounts


class AccountsForm(forms.ModelForm):
    class Meta:
        model = Accounts
        widgets = {
            'password': forms.PasswordInput(),
    }