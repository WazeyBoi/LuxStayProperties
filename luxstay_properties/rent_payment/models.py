# rent_payment/models.py
from django.db import models

class Payment(models.Model):
    paymentId = models.AutoField(primary_key=True)
    leaseId = models.ForeignKey('lease_management.Lease', on_delete=models.CASCADE)  # Assuming you want to store lease number or some unique identifier
    tenantId = models.CharField(max_length=100)  # Store tenant's name or identifier
    paymentDate = models.DateField()
    paymentMethod = models.CharField(max_length=100)
    totalAmount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50)

    def __str__(self):
        return f'Payment {self.paymentId} for Tenant {self.tenantId}'
