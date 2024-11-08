from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from users.models import User
from .models import Property
from .forms import PropertyForm

@login_required
def property_owner_dashboard(request):
    if request.user.role != 'property_owner':
        return redirect('login')  # Restrict access to PropertyOwners only
    return render(request, 'properties/dashboard.html')

@login_required
def property_listing_management(request):
    # Display only properties owned by the logged-in user
    properties = Property.objects.filter(owner=request.user)
    return render(request, 'properties/property_listing_management.html', {'properties': properties})

@login_required
def add_property(request):
    if request.method == "POST":
        form = PropertyForm(request.POST)
        if form.is_valid():
            property = form.save(commit=False)
            property.owner = request.user  # Set the property owner to the logged-in user
            property.save()
            return redirect('property_listing_management')
    else:
        form = PropertyForm()
    return render(request, 'properties/add_property.html', {'form': form})

@login_required
def update_property(request, property_id):
    property = get_object_or_404(Property, id=property_id, owner=request.user)
    if request.method == "POST":
        form = PropertyForm(request.POST, instance=property)
        if form.is_valid():
            form.save()
            return redirect('property_listing_management')
    else:
        form = PropertyForm(instance=property)
    return render(request, 'properties/update_property.html', {'form': form})

@login_required
def delete_property(request, property_id):
    property = get_object_or_404(Property, id=property_id, owner=request.user)
    if request.method == "POST":
        property.delete()
        return redirect('property_listing_management')
    return render(request, 'properties/delete_confirmation.html', {'property': property})

#test