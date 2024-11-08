# leases/views.py

from django.shortcuts import render, get_object_or_404, redirect
from datetime import date
from django.contrib.auth.decorators import login_required
from .models import Lease
from properties.models import Property

@login_required
def tenant_dashboard(request):
    # Fetch available properties for booking
    available_properties = Property.objects.filter(status='available')

    # Fetch the tenant’s bookings
    active_bookings = Lease.objects.filter(tenant=request.user, end_date__gte=date.today())
    old_bookings = Lease.objects.filter(tenant=request.user, end_date__lt=date.today())

    context = {
        'available_properties': available_properties,
        'active_bookings': active_bookings,
        'old_bookings': old_bookings,
    }
    
    return render(request, 'leases/tenant_dashboard.html', context)

@login_required
def book_property(request, property_id):
    property_obj = get_object_or_404(Property, id=property_id, status='available')
    
    if request.method == 'POST':
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        
        # Save the lease
        lease = Lease(
            tenant=request.user,
            property=property_obj,
            start_date=start_date,
            end_date=end_date,
        )
        lease.save()
        
        # Update property status to 'leased'
        property_obj.status = 'leased'
        property_obj.save()

        return redirect('tenant_dashboard')
    
    return render(request, 'leases/book_property.html', {'property': property_obj})

@login_required
def my_bookings(request):
    active_bookings = Lease.objects.filter(tenant=request.user, end_date__gte=date.today())
    old_bookings = Lease.objects.filter(tenant=request.user, end_date__lt=date.today())
    return render(request, 'leases/my_bookings.html', {'active_bookings': active_bookings, 'old_bookings': old_bookings})

#test