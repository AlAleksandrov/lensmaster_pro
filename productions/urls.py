from django.urls import path

from productions.views import CategoryListView, ProductionByCategoryListView, ProductionDetailView

urlpatterns = [
    path('categories/', CategoryListView.as_view(), name='category_list'),
    path('category/<slug:slug>/', ProductionByCategoryListView.as_view(), name='production_list_by_category'),
    path('production/<slug:slug>/', ProductionDetailView.as_view(), name='production_detail'),
]