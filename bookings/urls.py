from django.urls import path
from django.views.generic import TemplateView
from bookings.views import BookingCreateView

app_name = 'bookings'

urlpatterns = [
    path('request/', BookingCreateView.as_view(), name='booking_request'),
    path('success/', TemplateView.as_view(template_name='bookings/booking_success.html'), name='booking_success'),

]