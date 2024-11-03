from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import User

class CustomUserCreationForm(UserCreationForm):
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter password'}),
        help_text="Enter a strong password."
    )
    password2 = forms.CharField(
        label="Password confirmation",
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirm password'}),
        help_text="Enter the same password for verification."
    )

    class Meta:
        model = User
        fields = [
            'username', 
            'password1', 
            'password2', 
            'first_name', 
            'last_name', 
            'email', 
            'contact',
            'birthdate', 
            'streetAddress', 
            'city', 
            'zipcode'
        ]
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Enter username'}),
            'first_name': forms.TextInput(attrs={'placeholder': 'Enter first name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Enter last name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Enter email address'}),
            'contact': forms.TextInput(attrs={'placeholder': 'Enter contact number'}),
            'birthdate': forms.DateInput(attrs={'placeholder': 'YYYY-MM-DD', 'type': 'date'}),
            'streetAddress': forms.TextInput(attrs={'placeholder': 'Enter street address'}),
            'city': forms.TextInput(attrs={'placeholder': 'Enter city'}),
            'zipcode': forms.TextInput(attrs={'placeholder': 'Enter ZIP code'}),
        }
        
        # Removing default help text for username
        help_texts = {
            'username': None,
        }
