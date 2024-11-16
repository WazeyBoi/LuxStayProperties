from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.property_owner_dashboard, name='property_owner_dashboard'),
    path('property-listing-management/', views.property_listing_management, name='property_listing_management'),
    path('add-property/', views.add_property, name='add_property'),
    path('update-property/<int:property_id>/', views.update_property, name='update_property'),
    path('delete-property/<int:property_id>/', views.delete_property, name='delete_property'),
    path('property-bookings/', views.property_bookings, name='property_bookings'),
    path('terminate-confirmation/<int:lease_id>/', views.terminate_confirmation, name='terminate_confirmation'),
    path('terminate-lease/<int:lease_id>/', views.terminate_lease, name='terminate_lease'),
]
