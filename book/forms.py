from django.db import models
from django.forms import ModelForm
# from django.contrib.auth.models import User
# from cloudinary.models import CloudinaryField
from .models import Booking


class BookingForm(ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'

#    def__init__(self, *args, **kwargs):
#        guest = kwargs.pop('guest', None)
#        super()

# fields = ['booking_day', 'booking_time', 'number_of_guests', 'guest', 'guest_email', 'allergies']
