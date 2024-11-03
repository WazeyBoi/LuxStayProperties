from django.db import models
from users.models import User

class Property(models.Model):
    STATUS_CHOICES = [
        ('available', 'Available'),
        ('leased', 'Leased'),
    ]
    
    owner = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role': 'property_owner'})
    address = models.CharField(max_length=255)
    property_type = models.CharField(max_length=50)
    number_of_rooms = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='available')
    description = models.TextField(blank=True, null=True)
    listing_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.address} - {self.get_status_display()}"
