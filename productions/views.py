from django.contrib.auth.mixins import LoginRequiredMixin
from django.template.defaultfilters import slugify
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from productions.forms import ProductionForm
from productions.models import Category, Production


# Create your views here.
class CategoryListView(ListView):
    model = Category
    template_name = 'productions/category_list.html'
    context_object_name = 'categories'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = context.get('categories', context.get('object_list'))

        grouped_portfolio = []
        for category in categories:
            productions = Production.objects.filter(category=category)
            if productions.exists():
                grouped_portfolio.append({
                    'category': category,
                    'items': productions,
                })

        context['grouped_portfolio'] = grouped_portfolio
        context['production_create_url'] = reverse_lazy('productions:production_create')
        return context


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['related_productions'] = Production.objects.filter(
            category=self.object.category
        ).exclude(
            id=self.object.id
        )[:3]

        return context

class ProductionCreateView(CreateView):
    model = Production
    form_class = ProductionForm
    template_name = 'productions/production_form.html'
    success_url = reverse_lazy('productions:category_list')

    def form_valid(self, form):
        form.instance.slug = slugify(form.instance.title)
        return super().form_valid(form)

class ProductionUpdateView(UpdateView):
    model = Production
    form_class = ProductionForm
    template_name = 'productions/production_form.html'
    success_url = reverse_lazy('productions:category_list')

class ProductionDeleteView(DeleteView):
    model = Production
    template_name = 'productions/production_confirm_delete.html'
    success_url = reverse_lazy('productions:category_list')