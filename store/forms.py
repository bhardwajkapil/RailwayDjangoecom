from django import forms
from django.contrib.auth.models import User
from .models import Review
from django.contrib.auth.forms import UserCreationForm,UserChangeForm


class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=12,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'block w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-1 focus:ring-indigo-500',
            'placeholder': 'First Name',
        })
    )
    last_name = forms.CharField(
        max_length=12,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'block w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-1 focus:ring-indigo-500',
            'placeholder': 'Last Name',
        })
    )

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'block w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-1 focus:ring-indigo-500',
                'placeholder': 'Username',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'block w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-1 focus:ring-indigo-500',
                'placeholder': 'Email',
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget = forms.PasswordInput(attrs={
            'class': 'block w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-1 focus:ring-indigo-500',
            'placeholder': 'Password',
        })
        self.fields['password2'].widget = forms.PasswordInput(attrs={
            'class': 'block w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-1 focus:ring-indigo-500',
            'placeholder': 'Confirm Password',
        })



class UpdateUserForm(UserChangeForm):
    email = forms.EmailInput(attrs={
        'class': 'block w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-1 focus:ring-indigo-500',
        'placeholder': 'Email',
    })
    first_name = forms.CharField(
        max_length=12,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'block w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-1 focus:ring-indigo-500',
            'placeholder': 'First Name',
        })
    )
    last_name = forms.CharField(
        max_length=12,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'block w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-1 focus:ring-indigo-500',
            'placeholder': 'Last Name',
        })
    )

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')
        # No need to include or exclude 'password1' and 'password2' here

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Explicitly remove password fields from the form
        if 'password' in self.fields:
            del self.fields['password']
        if 'password1' in self.fields:
            del self.fields['password1']
        if 'password2' in self.fields:
            del self.fields['password2']
       
 
class ReviewForm(forms.ModelForm):
    class Meta:
        model=Review
        fields=['title', 'body', 'rating', 'image']
        widgets = {
            'rating': forms.NumberInput(attrs={
                'min': 1, 
                'max': 5, 
                'step': 1, 
                'class': 'form-control',
            }),
        }
   