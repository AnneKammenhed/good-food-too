from django.forms import ModelForm
from django.views.generic.edit import FormView

from django.views import generic, View

from django.db import models
from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import BookingForm


# view to see the bookings form FormView
class BookingFormView(FormView):
    template_name = 'index.html'
    form_class = BookingForm
    success_url = 'menu'

    def book(request):
        if request.method == 'POST':
            form = BookingForm(request.POST)
            if form.is_valid():
                return HttpResponseRedirect(reverse('menu'))
        else:
            form = BookingForm()
        
        return render(request, 'index.html', {"form": form})
