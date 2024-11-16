# lease_management/views.py
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Lease

class LeaseListView(ListView):
    model = Lease
    template_name = 'lease_management/lease_list.html'
    context_object_name = 'leases'

class LeaseCreateView(CreateView):
    model = Lease
    template_name = 'lease_management/lease_form.html'
    fields = '__all__'  # Specify the fields you want
    success_url = reverse_lazy('lease_list')  # Redirect to lease list after creation

class LeaseUpdateView(UpdateView):
    model = Lease
    template_name = 'lease_management/lease_form.html'
    fields = '__all__'  # or specify the fields you want
    success_url = reverse_lazy('lease_list')  # Redirect to lease list after creation\

class LeaseDeleteView(DeleteView):
    model = Lease
    template_name = 'lease_management/lease_confirm_delete.html'
    success_url = reverse_lazy('lease_list')
