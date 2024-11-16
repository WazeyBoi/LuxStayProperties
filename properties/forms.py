from django import forms
from .models import Property

class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = [
            'property_name',
            'address',
            'property_type',
            'number_of_rooms',
            'num_of_bathrooms',
            'price',
            'status',
            'description',
            'sqft',
            'is_furnished',
            'parking_spaces',
            'pet_policy',
        ]
        widgets = {
            'property_type': forms.Select(attrs={
                'class': 'form-control',  # Optional styling
            }),
        }
