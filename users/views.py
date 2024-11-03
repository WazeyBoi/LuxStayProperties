from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import User
from leases.models import Lease
from .forms import CustomUserCreationForm

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

@login_required
def tenant_management(request):
    tenants = []
    search_query = request.GET.get("search", "").strip()  # Get the search term from query parameters

    if search_query:
        # Filter only tenants by first name or last name, case-insensitively
        tenants = User.objects.filter(
            role='tenant',  # Ensures we retrieve only tenants
        ).filter(
            first_name__icontains=search_query
        ) | User.objects.filter(
            role='tenant',
            last_name__icontains=search_query
        )

    return render(request, 'users/tenant_management.html', {'tenants': tenants})

@login_required
def tenant_landing_page(request):
    # Check if the logged-in user has the role 'tenant'
    if request.user.role != 'tenant':
        return redirect('login')  # Redirect to login or another page if the user is not a tenant

    return render(request, 'users/tenant_landing_page.html')

