from django.shortcuts import render
# from django.views.generic.edit import FormView
# from django import forms
from django.views import generic
from .models import Booking

# view to see the bookings tried FormView 
class BookingView(generic.ListView):
    template_name = 'index.html'
    model = Booking
    queryset = Booking.objects.order_by("-booking_day")
#    success_url = '/Thanks for booking!/'

#    def form_valid(self, form):
#        form.send_email()
#        return super().form_valid(form)
