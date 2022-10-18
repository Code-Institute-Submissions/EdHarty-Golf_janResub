from .models import Teetime, UserAccount
from django import forms
from django.forms import ModelForm, CharField, TextInput


class UpdateBookingDetails(forms.ModelForm):
    class Meta:
        model = Booking
        fields = (
            'booking_date', 'booking_time', 'player_count', 'booking_comments')


class EditAccountForm(forms.ModelForm):

    phone_number = CharField(widget=TextInput(attrs={'type': 'number'}))
    
    class Meta:
        model = UserAccount()
        fields = ('first_name', 'last_name', 'phone_number')
