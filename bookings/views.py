from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from bookings.forms import BookingRequestForm
from bookings.models import BookingRequest

# Create your views here.
class BookingCreateView(CreateView):
    model = BookingRequest
    form_class = BookingRequestForm
    template_name = 'bookings/booking_form.html'
    success_url = reverse_lazy('bookings:booking_success')