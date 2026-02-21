from django.urls import path, include
from productions.views import CategoryListView, ProductionByCategoryListView, ProductionDetailView, \
    ProductionCreateView, ProductionUpdateView, ProductionDeleteView

app_name = 'productions'

productions_patterns = [
    path('', ProductionDetailView.as_view(), name='production_detail'),
    path('edit/', ProductionUpdateView.as_view(), name='production_edit'),
    path('delete/', ProductionDeleteView.as_view(), name='production_delete'),
]

urlpatterns = [
    path('add/', ProductionCreateView.as_view(), name='production_create'),
    path('categories/', CategoryListView.as_view(), name='category_list'),
    path('category/<slug:slug>/', ProductionByCategoryListView.as_view(), name='production_list_by_category'),
    path('production/<slug:slug>/', include(productions_patterns)),
]