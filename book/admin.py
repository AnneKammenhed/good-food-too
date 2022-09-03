from django import forms
from django.contrib import admin
from .models import Booking

# class CustomBookingAdmin(admin.ModelAdmin):
#    form = Booking

#    class Meta:
#        model = Booking
#        fields = '__all__'
        

# add Booking model to admin panel
@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    pass

# ['booking_day', 'booking_time', 'number_of_guests', 'guest', 'guest_email', 'allergies']
# admin.site.register(Booking, CustomBookingAdmin)
