from django.urls import path
from inventory.views import EquipmentListView

app_name = 'inventory'

urlpatterns = [
    path('', EquipmentListView.as_view(), name='equipment_list'),
]