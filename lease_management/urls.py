# lease_management/urls.py
from django.urls import path
from .views import LeaseListView, LeaseCreateView, LeaseUpdateView, LeaseDeleteView

urlpatterns = [
    path('', LeaseListView.as_view(), name='lease_list'),
    path('create/', LeaseCreateView.as_view(), name='lease_create'),
    path('<int:pk>/update/', LeaseUpdateView.as_view(), name='lease_update'),
    path('<int:pk>/delete/', LeaseDeleteView.as_view(), name='lease_delete'),
]
