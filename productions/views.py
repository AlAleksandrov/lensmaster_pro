from django.shortcuts import render
from django.views.generic import ListView, DetailView

from productions.models import Category, Production


# Create your views here.
class CategoryListView(ListView):
    model = Category
    template_name = 'productions/category_list.html'
    context_object_name = 'categories'


class ProductionByCategoryListView(ListView):
    model = Production
    template_name = 'productions/production_list.html'
    context_object_name = 'productions'

    def get_queryset(self):
        return Production.objects.filter(category__slug=self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.get(slug=self.kwargs['slug'])
        return context


class ProductionDetailView(DetailView):
    model = Production
    template_name = 'productions/production_detail.html'
    context_object_name = 'production'