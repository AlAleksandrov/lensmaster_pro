from django.urls import path, include
from django.views.generic import TemplateView
from bookings import views
from bookings.views import BookingCreateView

app_name = 'bookings'

bookings_patterns = [
    path('', views.ServicePackageListView.as_view(), name='package_list'),
    path('create/', views.ServicePackageCreateView.as_view(), name='package_create'),
    path('<int:pk>/', include([
        path('', views.ServicePackageDetailView.as_view(), name='package_detail'),
        path('edit/', views.ServicePackageUpdateView.as_view(), name='package_edit'),
        path('delete/', views.ServicePackageDeleteView.as_view(), name='package_delete'),
    ])),
]

urlpatterns = [

    path('request/', BookingCreateView.as_view(), name='booking_request'),
    path('success/', TemplateView.as_view(template_name='bookings/booking_success.html'), name='booking_success'),
    path('packages/', include(bookings_patterns)),

]