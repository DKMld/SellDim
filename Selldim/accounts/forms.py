from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from Selldim.accounts.models import ProfilePicture


class AccountsForm(UserCreationForm):

    class Meta:
        model = User

        fields = ['username', 'email', 'password1', 'password2']


class AccountsEditForm(AccountsForm):
    class Meta:
        model = User

        fields = ['username', 'email', 'first_name', 'last_name']


class AddProfilePicture(ModelForm):
    class Meta:
        model = ProfilePicture

        fields = ['user_picture']
