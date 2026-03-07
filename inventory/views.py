from django.views.generic import ListView, DetailView
from inventory.models import Equipment


# Create your views here.
class EquipmentListView(ListView):
    model = Equipment
    template_name = 'inventory/equipment_list.html'
    context_object_name = 'equipment_list'
    paginate_by = 4

    def get_queryset(self):
        return Equipment.objects.filter(is_active=True).prefetch_related('productions')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        qs = self.get_queryset()

        types = Equipment.EquipmentType.choices

        grouped = []
        for val, label in types:
            items = qs.filter(equipment_type=val)
            if items.exists():
                grouped.append({
                    'type': label,
                    'items': items,
                })

        context['grouped_equipment'] = grouped

        return context


class EquipmentDetailView(DetailView):
    model = Equipment
    template_name = 'inventory/equipment_detail.html'
    context_object_name = 'item'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['productions'] = self.object.productions.all().select_related('category')

        return context
