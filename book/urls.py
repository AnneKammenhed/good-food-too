from . import views
from django.urls import path


urlpatterns = [
    path('', views.BookingFormView.as_view(), name='home'),
]

# path('', views.BookingView.as_view(), name='book'),
