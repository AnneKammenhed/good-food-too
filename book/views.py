from django.shortcuts import render, get_object_or_404, reverse
from django.views.generic.edit import FormView
# from django import forms
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Booking
from .forms import BookingForm


# view to see the bookings
class BookingView(generic.ListView):
    template_name = 'index.html'
    model = Booking
    queryset = Booking.objects.order_by("-booking_day")

# view to see the bookings form FormView
class BookingFormView(FormView):
    template_name = 'index.html'
    form_class = BookingForm
    success_url = '/Thanks for booking!/'


#    def form_valid(self, form):
#        booking = booking.objects.create_booking(
#            booking_day=form.cleaned_data['booking_day']
#        )
#
#        return super(BookingFormView, self).form_valid(form)
