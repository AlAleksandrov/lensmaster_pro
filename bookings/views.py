from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView
from bookings.forms import BookingRequestForm, ServicePackageForm
from bookings.models import BookingRequest, ServicePackage


# Create your views here.
class BookingCreateView(CreateView):
    model = BookingRequest
    form_class = BookingRequestForm
    template_name = 'bookings/booking_form.html'
    success_url = reverse_lazy('bookings:booking_success')


class ServicePackageListView(ListView):
    model = ServicePackage
    template_name = 'bookings/package_list.html'
    context_object_name = 'packages'

    def get_queryset(self):
        return super().get_queryset().filter(is_active=True).order_by('category__name', 'price')


class ServicePackageCreateView(CreateView):
    model = ServicePackage
    form_class = ServicePackageForm
    template_name = 'bookings/package_form.html'
    success_url = reverse_lazy('bookings:package_list')


class ServicePackageUpdateView(UpdateView):
    model = ServicePackage
    form_class = ServicePackageForm
    template_name = 'bookings/package_form.html'
    success_url = reverse_lazy('bookings:package_list')