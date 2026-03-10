from django.urls import path, include
from inventory.views import EquipmentListView, EquipmentDetailView, EquipmentCreateView, EquipmentUpdateView, \
    EquipmentDeleteView

app_name = 'inventory'

urlpatterns = [
    path('', EquipmentListView.as_view(), name='equipment_list'),
    path('add/', EquipmentCreateView.as_view(), name='equipment_create'),
    path('<int:pk>/', include([
        path('', EquipmentDetailView.as_view(), name='equipment_detail'),
        path('edit/', EquipmentUpdateView.as_view(), name='equipment_edit'),
        path('delete/', EquipmentDeleteView.as_view(), name='equipment_delete'),
        ])
    ),
]