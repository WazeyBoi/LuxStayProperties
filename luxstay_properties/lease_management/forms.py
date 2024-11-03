# lease_management/forms.py
from django import forms
from .models import Lease

class LeaseForm(forms.ModelForm):
    class Meta:
        model = Lease
        fields = ['propertyId', 'tenantId', 'startDate', 'endDate', 'totalAmount']
