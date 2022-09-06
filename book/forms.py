from django.db import models
from django import forms
from .models import Booking
from django.forms import ModelForm


class BookingForm(ModelForm):

    class Meta:
        model = Booking
        fields = [
            'booking_day', 
            'booking_time', 
            'number_of_guests', 
            'guest_email',
            'allergies',
        ]
        
        labels = {
            'booking_day': 'Booking day',
            'booking_time': 'Booking time',
            'number_of_guests': 'Max 8 guests online',
            'guest_email': 'Your email address',
            'allergies': 'Any allergies?'
        }


#        fields = '__all__'


# forms.Form
#    guest = forms.CharField(max_length=100)
#    email = forms.EmailField()
