from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from bookings.forms import BookingRequestForm, ServicePackageForm
from bookings.models import BookingRequest, ServicePackage


# Create your views here.
class BookingCreateView(CreateView):
    model = BookingRequest
    form_class = BookingRequestForm
    template_name = 'bookings/booking_form.html'
    success_url = reverse_lazy('bookings:booking_success')

    def get_form(self, form_class = None):
        form = super().get_form(form_class)
        package_id = self.request.GET.get('package')
        if package_id:
            form.fields['package'].initial = package_id
        return form


class ServicePackageListView(ListView):
    model = ServicePackage
    template_name = 'bookings/package_list.html'
    context_object_name = 'packages'

    def get_queryset(self):
        return super().get_queryset().filter(is_active=True).order_by('category__name', 'price')


class ServicePackageDetailView(DetailView):
    model = ServicePackage
    template_name = 'bookings/package_detail.html'
    context_object_name = 'package'


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


class ServicePackageDeleteView(DeleteView):
    model = ServicePackage
    template_name = 'bookings/package_confirm_delete.html'
    success_url = reverse_lazy('bookings:package_list')

