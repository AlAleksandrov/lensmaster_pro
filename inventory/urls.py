from django.urls import path
from inventory.views import EquipmentListView, EquipmentDetailView

app_name = 'inventory'

urlpatterns = [
    path('', EquipmentListView.as_view(), name='equipment_list'),
    path('<int:pk>/', EquipmentDetailView.as_view(), name='equipment_detail'),
]