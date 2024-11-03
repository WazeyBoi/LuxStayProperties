from django.urls import path
from . import views

urlpatterns = [
    path('tenant_dashboard/', views.tenant_dashboard, name='tenant_dashboard'),
    path('book_property/<int:property_id>/', views.book_property, name='book_property'),
    path('my_bookings/', views.my_bookings, name='my_bookings'),
]
