from django.urls import path, include
from inventory import views

app_name = 'inventory'

urlpatterns = [
    path('', views.EquipmentListView.as_view(), name='equipment_list'),
    path('create/', views.EquipmentCreateView.as_view(), name='equipment_create'),
    path('<int:pk>/', include([
        path('', views.EquipmentDetailView.as_view(), name='equipment_detail'),
        path('edit/', views.EquipmentUpdateView.as_view(), name='equipment_edit'),
        path('delete/', views.EquipmentDeleteView.as_view(), name='equipment_delete'),
        ]),
    ),
]