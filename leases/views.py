# leases/views.py

from django.shortcuts import render, get_object_or_404, redirect
from datetime import date
from django.contrib.auth.decorators import login_required
from .models import Lease
from properties.models import Property
from datetime import datetime

@login_required
def tenant_dashboard(request):
    # Filter leases based on status
    active_leases = Lease.objects.filter(tenant=request.user, status='active', end_date__gte=date.today())
    inactive_leases = Lease.objects.filter(tenant=request.user, status='inactive')

    context = {
        'active_leases': active_leases,
        'inactive_leases': inactive_leases,
    }
    return render(request, 'leases/tenant_dashboard.html', context)

@login_required
def book_property(request, property_id):
    property_obj = get_object_or_404(Property, id=property_id, status='available')
    
    if request.method == 'POST':
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        
        # Use the property's monthly price as the total amount
        total_amount = property_obj.price

        # Save the lease
        lease = Lease(
            tenant=request.user,
            property=property_obj,
            start_date=start_date,
            end_date=end_date,
            total_amount=total_amount,
            status='active'
        )
        lease.save()
        
        # Update property status to 'leased'
        property_obj.status = 'leased'
        property_obj.save()

        return redirect('tenant_dashboard')
    
    return render(request, 'leases/book_property.html', {'property': property_obj})

@login_required
def my_bookings(request):
    active_bookings = Lease.objects.filter(tenant=request.user, status='active')
    old_bookings = Lease.objects.filter(tenant=request.user, status__in=['inactive', 'terminated'])
    return render(request, 'leases/my_bookings.html', {'active_bookings': active_bookings, 'old_bookings': old_bookings})

@login_required
def property_listing(request):
    available_properties = Property.objects.filter(status='available')
    return render(request, 'properties/property_listing.html', {'properties': available_properties})

@login_required
def view_property_details(request, property_id):
    # Retrieve the property by ID
    property = get_object_or_404(Property, id=property_id)

    # Pass the property to the template
    return render(request, 'properties/view_property_details.html', {'property': property})

#test