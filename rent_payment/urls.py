# rent_payment/urls.py
from django.urls import path
from .views import payment_list, payment_create, payment_update, payment_delete

urlpatterns = [
    path('payment-list', payment_list, name='payment_list'),
    path('create/', payment_create, name='payment_create'),
    path('update/<int:paymentId>/', payment_update, name='payment_update'),
    path('delete/<int:paymentId>/', payment_delete, name='payment_delete'),
]
