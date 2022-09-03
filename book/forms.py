from django.db import models
from django import forms
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'
