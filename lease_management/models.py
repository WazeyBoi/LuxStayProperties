# lease_management/models.py
from django.db import models

class Lease(models.Model):
    leaseId = models.AutoField(primary_key=True)
    propertyId = models.CharField(max_length=100)  # Use appropriate field type
    tenantId = models.CharField(max_length=100)     # Use appropriate field type
    startDate = models.DateField()
    endDate = models.DateField()
    totalAmount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'Lease {self.leaseId} for Property {self.propertyId}'
