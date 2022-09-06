from django.db import models
from django import forms
from .models import Booking
from django.forms import ModelForm


class BookingForm(ModelForm):

    class Meta:
        model = Booking
        fields = ['booking_day']
        labels = {'booking_day': 'Booking day'}


#        fields = '__all__'


# forms.Form
    guest = forms.CharField(max_length=100)
    email = forms.EmailField()
