from django.urls import path, include
from productions.views import CategoryListView, CategoryCreateView, CategoryUpdateView, CategoryDeleteView, \
    ProductionByCategoryListView, ProductionDetailView, ProductionCreateView, ProductionUpdateView, ProductionDeleteView

app_name = 'productions'

productions_patterns = [
    path('', ProductionDetailView.as_view(), name='production_detail'),
    path('edit/', ProductionUpdateView.as_view(), name='production_edit'),
    path('delete/', ProductionDeleteView.as_view(), name='production_delete'),
]

category_patterns = [
    path('edit/', CategoryUpdateView.as_view(), name='category_edit'),
    path('delete/', CategoryDeleteView.as_view(), name='category_delete'),
]

urlpatterns = [
    path('add/', ProductionCreateView.as_view(), name='production_create'),
    path('categories/', include([
            path('', CategoryListView.as_view(), name='category_list'),
            path('add/', CategoryCreateView.as_view(), name='category_create'),
            path('<slug:slug>/', include(category_patterns)),
        ])),
    path('category/<slug:slug>/', ProductionByCategoryListView.as_view(), name='production_list_by_category'),
    path('production/<slug:slug>/', include(productions_patterns)),
]