from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={
            'id': 'username',
            'class': 'form-input',
            'placeholder': ' '
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'id': 'password',
            'class': 'form-input',
            'placeholder': ' '
        })
    )

class RegisterForm(UserCreationForm):
    """
    Registration form that extends Django's UserCreationForm to include all required fields
    """
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={
            'class': 'form-input',
            'placeholder': ' '
        })
    )
    first_name = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={
            'class': 'form-input',
            'placeholder': ' '
        })
    )
    last_name = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={
            'class': 'form-input',
            'placeholder': ' '
        })
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-input',
            'placeholder': ' '
        })
    )
    mobile_number = forms.CharField(
        max_length=15,
        widget=forms.TextInput(attrs={
            'class': 'form-input',
            'placeholder': ' '
        })
    )
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={
            'class': 'form-input',
            'placeholder': ' '
        })
    )
    password2 = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput(attrs={
            'class': 'form-input',
            'placeholder': ' '
        })
    )

    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'mobile_number', 'password1', 'password2')
