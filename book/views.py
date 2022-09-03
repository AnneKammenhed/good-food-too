from django.shortcuts import render
from django.views.generic.edit import FormView
from django import forms
from .models import Booking

# view to see the bookings
class BookingForm(FormView):
    template = 'index.html'
    form = Booking()
    success_url = '/Thanks for booking!/'

    def form_valid(self, form):
        form.send_email()
        return super().form_valid(form)
