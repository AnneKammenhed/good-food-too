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
class BookingFormView(FormView):
    template_name = 'index.html'
    form_class = BookingForm
    model = Booking
    success_url = '/home/'

    def add_booking(request):
        submitted = False 
        if request.method == 'POST':
            form = BookingForm(request.POST) 
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('home?submitted=True')
        else:
            form = BookingForm
            if 'submitted' in request.GET:
                submitted = True
        
        return render(request, 'index.html', {"form": form_class, 'submitted':sumbitted})
