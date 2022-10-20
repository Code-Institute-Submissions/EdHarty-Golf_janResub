from .models import Teetime, UserAccount
from django import forms
from django.forms import ModelForm, CharField, TextInput


class UpdateTeetimeDetails(forms.ModelForm):
    class Meta:
        model = Teetime
        fields = (
            'teetime_date', 'teetime_time', 'player_count', 'teetime_comments')


class EditAccountForm(forms.ModelForm):

    phone_number = CharField(widget=TextInput(attrs={'type': 'number'}))
   
    class Meta:
        model = UserAccount()
        fields = ('first_name', 'last_name', 'phone_number')
