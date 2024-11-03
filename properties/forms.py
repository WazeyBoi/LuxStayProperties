from django import forms
from .models import Property

class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ['address', 'property_type', 'number_of_rooms', 'price', 'status', 'description']
