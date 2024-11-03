from django.shortcuts import render, redirect, get_object_or_404
from .models import MaintenanceRequest
from .forms import MaintenanceRequestForm

def maintenance_list(request):
    requests = MaintenanceRequest.objects.all()
    return render(request, 'Maintenance_Request/maintenance_list.html', {'requests': requests})

def maintenance_create(request):
    if request.method == 'POST':
        form = MaintenanceRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('maintenance_list')
    else:
        form = MaintenanceRequestForm()
    return render(request, 'Maintenance_Request/maintenance_form.html', {'form': form})

def maintenance_update(request, pk):
    request_obj = get_object_or_404(MaintenanceRequest, pk=pk)
    if request.method == 'POST':
        form = MaintenanceRequestForm(request.POST, instance=request_obj)
        if form.is_valid():
            form.save()
            return redirect('maintenance_list')
    else:
        form = MaintenanceRequestForm(instance=request_obj)
    return render(request, 'Maintenance_Request/maintenance_form.html', {'form': form})

def maintenance_delete(request, pk):
    request_obj = get_object_or_404(MaintenanceRequest, pk=pk)
    if request.method == 'POST':
        request_obj.delete()
        return redirect('maintenance_list')
    return render(request, 'Maintenance_Request/maintenance_confirm_delete.html', {'object': request_obj})
