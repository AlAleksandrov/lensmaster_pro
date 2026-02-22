from django.views.generic import ListView, DetailView
from inventory.models import Equipment


# Create your views here.
class EquipmentListView(ListView):
    model = Equipment
    template_name = 'inventory/equipment_list.html'
    context_object_name = 'equipment_items'

    def get_queryset(self):
        qs = Equipment.objects.filter(is_active=True).order_by('equipment_type')

        selected_type = self.request.GET.get('type')
        if selected_type:
            qs = qs.filter(equipment_type__iexact=selected_type)

        try:
            qs = qs.prefetch_related('productions')
        except AttributeError:
            pass

        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        ordered_types = ['Camera', 'Lens', 'Lighting', 'Drone', 'Other']

        context['selected_type'] = self.request.GET.get('type')

        grouped = {}
        for item in context['equipment_items']:
            label = item.get_equipment_type_display()
            if label not in grouped:
                grouped[label] = []
            grouped[label].append(item)

        grouped_equipment = [{
            'type': t,
            'items': grouped[t]
        }
            for t in ordered_types
            if t in grouped
        ]

        context['grouped_equipment'] = grouped_equipment

        return context


class EquipmentDetailView(DetailView):
    model = Equipment
    template_name = 'inventory/equipment_detail.html'
    context_object_name = 'item'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        item = self.object

        if hasattr(item, 'productions'):
            productions = item.productions.all()
        else:
            productions = getattr(item, 'production_set', item.__class__).all() if hasattr(item, '__class__') else []

        context['productions'] = productions

        return context
