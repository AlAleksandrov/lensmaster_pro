from django.urls import path, include
from django.views.generic import TemplateView
from bookings import views
from bookings.views import BookingCreateView

app_name = 'bookings'

bookings_patterns = [
    path('', views.ServicePackageListView.as_view(), name='package_list'),
    path('add/', views.ServicePackageCreateView.as_view(), name='package_create'),
    path('<int:pk>/edit/', views.ServicePackageUpdateView.as_view(), name='package_edit'),
]

urlpatterns = [

    path('request/', BookingCreateView.as_view(), name='booking_request'),
    path('success/', TemplateView.as_view(template_name='bookings/booking_success.html'), name='booking_success'),
    path('packages/', include(bookings_patterns)),

]