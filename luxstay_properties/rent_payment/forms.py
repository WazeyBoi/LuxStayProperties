# rent_payment/forms.py
from django import forms
from .models import Payment

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['leaseId', 'tenantId', 'paymentDate', 'paymentMethod', 'totalAmount', 'status']
