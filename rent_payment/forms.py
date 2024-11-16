# rent_payment/forms.py
from django import forms
from .models import Payment

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['leaseId', 'tenantId', 'paymentDate', 'paymentMethod', 'totalAmount', 'status']
    
    # Optionally, you can customize the widget if desired
    paymentMethod = forms.ChoiceField(
        choices=Payment.PAYMENT_METHOD_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

        # Add a custom widget for the paymentDate field
    paymentDate = forms.DateField(
        widget=forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'})
    )

    status = forms.ChoiceField(
        choices=Payment.STATUS_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
