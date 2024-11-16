from django.urls import path
from . import views

urlpatterns = [
    path('tenant_dashboard/', views.tenant_dashboard, name='tenant_dashboard'),
    path('book_property/<int:property_id>/', views.book_property, name='book_property'),
    path('my_bookings/', views.my_bookings, name='my_bookings'),
    path('property-listing/', views.property_listing, name='property_listing'),
    path('view-details/<int:property_id>/', views.view_property_details, name='view_property_details'),
]
