from django.forms import ModelForm
from django.views.generic.edit import FormView

from django.views import generic, View

from django.db import models
from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import BookingForm
from .models import Booking

# view to see the bookings form FormView
# class BookingFormView(FormView):
#    template_name = 'bookings.html'
#    model = Booking
#    success_url = '/home/'

# function to add valid bookings to the database
def add_booking(request):
    submitted = False
    if request.method == 'POST':
        booking_form = BookingForm(request.POST)
        if booking_form.is_valid():
            booking_form.save()
            return HttpResponseRedirect('bookings?submitted=True')
    else:
        booking_form = BookingForm
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'bookings.html', {'form': booking_form, 'submitted': submitted})

def home(request):
    return render(request, 'index.html')

def menu(request):
    return render(request, 'menu.html')
