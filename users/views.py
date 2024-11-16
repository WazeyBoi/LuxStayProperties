from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import User
from leases.models import Lease
from .forms import CustomUserCreationForm
from datetime import date
from django.contrib import messages

def register_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login page after successful registration
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html', {'form': form})

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                
                # Redirect based on user role
                if user.role == 'tenant':
                    return redirect('tenant_dashboard')  # Redirect tenants to the tenant dashboard
                elif user.role == 'property_owner':
                    return redirect('property_owner_dashboard')  # Redirect property owners to their dashboard
                
                # Default redirect (if needed)
                return redirect('home')  # Replace 'home' with a suitable default page if needed
                
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to login page after logout

from django.db.models import Q
from datetime import date

@login_required
def tenant_management(request):
    tenants = None
    search_query = request.GET.get("search", "").strip()

    if search_query:
        # Filter tenants by first name or last name, excluding superusers
        tenants = User.objects.filter(
            role='tenant',
            is_superuser=False
        ).filter(
            Q(first_name__icontains=search_query) | Q(last_name__icontains=search_query)
        )
    else:
        # Default to showing all tenants, excluding superusers
        tenants = User.objects.filter(
            role='tenant',
            is_superuser=False
        )

    # Add active and inactive leases for each tenant
    for tenant in tenants:
        tenant.active_leases = Lease.objects.filter(tenant=tenant, end_date__gte=date.today())
        tenant.inactive_leases = Lease.objects.filter(tenant=tenant, end_date__lt=date.today())

    return render(request, 'users/tenant_management.html', {'tenants': tenants})

@login_required
def tenant_landing_page(request):
    # Check if the logged-in user has the role 'tenant'
    if request.user.role != 'tenant':
        return redirect('login')  # Redirect to login or another page if the user is not a tenant

    return render(request, 'users/tenant_landing_page.html')

@login_required
def view_tenant_lease(request, tenant_id):
    tenant = get_object_or_404(User, id=tenant_id, role='tenant')

    # Fetch active and inactive leases
    active_leases = Lease.objects.filter(tenant=tenant, status='active')
    inactive_leases = Lease.objects.filter(tenant=tenant, status='inactive')

    # Pass data to the template
    context = {
        'tenant': tenant,
        'active_leases': active_leases,
        'inactive_leases': inactive_leases,
    }
    return render(request, 'users/view_lease.html', context)

@login_required
def edit_account(request):
    user = request.user  # Fetch the currently logged-in user
    if request.method == 'POST':
        # Update all user details
        user.username = request.POST.get('username', user.username)
        user.first_name = request.POST.get('first_name', user.first_name)
        user.last_name = request.POST.get('last_name', user.last_name)
        user.email = request.POST.get('email', user.email)
        user.phone = request.POST.get('phone', user.phone)
        user.address = request.POST.get('address', user.address)  # Assuming you have an address field
        user.city = request.POST.get('city', user.city)
        user.zip_code = request.POST.get('zip_code', user.zip_code)
        user.save()

        messages.success(request, "Your account details have been updated.")
        return redirect('tenant_dashboard')  # Redirect after updating

    return render(request, 'users/edit_account.html', {'user': user})