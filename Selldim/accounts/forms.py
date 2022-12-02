from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm, FileInput, TextInput, ChoiceField
from Selldim.accounts.models import ProfilePicture, UserComments


class AccountsForm(UserCreationForm):

    class Meta:
        model = User

        fields = ['username', 'email', 'password1', 'password2']


class AccountsEditForm(ModelForm):

    class Meta:
        model = User

        fields = ['username', 'email', 'first_name', 'last_name']
        exclude = ['password1', 'password2']


class AddProfilePicture(ModelForm):

    class Meta:
        model = ProfilePicture

        fields = ['user_picture']

        widgets = {
            'user_picture': FileInput(
                attrs={
                    'class': 'profile--picture--form',
                    'onchange': 'readURL(this);',
                }
            )
        }


class LeaveComment(ModelForm):
    class Meta:
        model = UserComments
        fields = '__all__'

        widgets = {
            'comment': TextInput(attrs={
                'id': 'input',
                'class': 'publisher-input',
                'type': 'text',
                'placeholder': 'Write something',
            }),


        }

