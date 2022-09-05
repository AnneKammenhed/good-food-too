# from django.shortcuts import render #, get_object_or_404, reverse

from django.forms import ModelForm
from django.views.generic.edit import FormView

from django.views import generic, View
# from django.http import HttpResponseRedirect
# from django.db import models

# from django.db import models
from django import forms

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
    success_url = 'menu'

    def form (self, request):

        return render (
            request,
            'index.html',
            {
            "booking_form": BookingForm()
            },
        )

#        if request.method == 'POST':
#            form = BookingForm(request.POST)
#            if form.is_valid():
#                form_data = form.cleaned_data
#                message = f'Thank you {form_data[guest]}'
#        else:
#            form = BookingForm()
#        
#        return render(request, 'index.html', {"book": form})

#    def post(self, request, *args, **kwargs):

#        post = get_object_or_404(Booking, guest=guest)
#        (data=request.POST)

#        booking = booking.objects.create_booking(
#            booking_day=form.cleaned_data['booking_day']
#        )
#
#        return super(BookingFormView, self).form_valid(form)
