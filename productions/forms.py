from django import forms
from .models import Production


class ProductionForm(forms.ModelForm):
    class Meta:
        model = Production
        fields = ['title', 'category', 'location', 'cover_image', 'date_created', 'short_description', 'description', 'is_featured', 'equipment']

        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control bg-dark text-white border-secondary',
                    'placeholder': 'Enter project title'
                }
            ),
            'category': forms.Select(
                attrs={
                    'class': 'form-select bg-dark text-white border-secondary'
                }
            ),
            'location': forms.TextInput(
                attrs={
                    'class': 'form-control bg-dark text-white border-secondary',
                    'placeholder': 'e.g Sofia, Bulgaria'
                }
            ),
            'date_created': forms.DateInput(
                attrs={
                    'type': 'date',
                    'class': 'form-control bg-dark text-white border-secondary'
                }
            ),
            'short_description': forms.TextInput(
                attrs={
                    'class': 'form-control bg-dark text-white border-secondary',
                    'placeholder': 'Brief summary...'
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'class': 'form-control bg-dark text-white border-secondary',
                    'rows': 5,
                    'placeholder': 'Detailed project description...'
                }
            ),
            'cover_image': forms.FileInput(
                attrs={
                    'class': 'form-control bg-dark text-white border-secondary'
                }
            ),
            'is_featured': forms.CheckboxInput(
                attrs={
                    'class': 'form-check-input'
                }
            ),
            'equipment': forms.CheckboxSelectMultiple(
                attrs={
                    'class': 'equipment-checkbox-list',
                }
            ),
        }
