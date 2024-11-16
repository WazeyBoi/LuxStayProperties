from django.db import models
from users.models import User

class Property(models.Model):
    STATUS_CHOICES = [
        ('available', 'Available'),
        ('leased', 'Leased'),
    ]

    PROPERTY_TYPE_CHOICES = [
    ('apartment', 'Apartment'),
    ('house', 'House'),
    ('condo', 'Condominium'),
    ('townhouse', 'Townhouse'),
    ('studio', 'Studio'),
    ]
    
    owner = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role': 'property_owner'})
    address = models.CharField(max_length=255)
    property_name = models.CharField(max_length=100, default= '')
    property_type = models.CharField(max_length=50, choices=PROPERTY_TYPE_CHOICES, default='apartment')
    number_of_rooms = models.PositiveIntegerField(default=1)
    num_of_bathrooms = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='available')
    description = models.TextField(blank=True, null=True)
    listing_date = models.DateField(auto_now_add=True)
    sqft = models.PositiveIntegerField(default=0)
    is_furnished = models.BooleanField(default=False)
    parking_spaces = models.PositiveIntegerField(default=0)
    pet_policy = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.property_name or self.address} - {self.get_status_display()}"
