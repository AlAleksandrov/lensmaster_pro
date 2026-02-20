from django.shortcuts import render
from django.views.generic import ListView
from inventory.models import Equipment

# Create your views here.
class EquipmentListView(ListView):
    model = Equipment
    template_name = 'inventory/equipment_list.html'
    context_object_name = 'equipment_items'

    def get_queryset(self):
        return Equipment.objects.filter(is_active=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        ordered_types = ['Camera', 'Lens', 'Lighting', 'Drone', 'Other']

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