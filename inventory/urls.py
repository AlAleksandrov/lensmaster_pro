from django.urls import path
from inventory.views import EquipmentListView

urlpatterns = [
    path('', EquipmentListView.as_view(), name='equipment_list'),
]