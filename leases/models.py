from django.db import models
from users.models import User
from properties.models import Property

class Lease(models.Model):
    tenant = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role': 'tenant'})
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"Lease {self.id} - {self.property.address} by {self.tenant.username}"
