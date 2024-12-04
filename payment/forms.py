from django import forms
from django.contrib.auth.models import User
from .models import ShippingAddress

class ShippingAddressForm(forms.ModelForm):
     shipping_full_name = forms.CharField(
        max_length=50, required=True, widget=forms.TextInput(attrs={
            'class': 'block w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-1 focus:ring-indigo-500',
            'placeholder': 'Full Name',
        })
    )
     shipping_phone = forms.CharField(
        max_length=13, required=True, widget=forms.TextInput(attrs={
            'class': 'block w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-1 focus:ring-indigo-500',
            'placeholder': 'Shipping Phone',
        })
    )
     shipping_email = forms.EmailField(
        max_length=13, required=True, widget=forms.TextInput(attrs={
            'class': 'block w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-1 focus:ring-indigo-500',
            'placeholder': 'Shipping Email',
        })
    )
     
     shipping_address1 = forms.CharField(
        max_length=100, required=True, widget=forms.TextInput(attrs={
            'class': 'block w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-1 focus:ring-indigo-500',
            'placeholder': ' shipping adress1',
        })
    )
     shipping_address2 = forms.CharField(
        max_length=100, widget=forms.TextInput(attrs={
            'class': 'block w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-1 focus:ring-indigo-500',
            'placeholder': 'shipping adress2',
        })
    )
     
     shipping_city = forms.CharField(
        max_length=30, required=True, widget=forms.TextInput(attrs={
            'class': 'block w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-1 focus:ring-indigo-500',
            'placeholder': ' shipping City',
        })
    )
     shipping_state = forms.CharField(
        max_length=40, required=True, widget=forms.TextInput(attrs={
            'class': 'block w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-1 focus:ring-indigo-500',
            'placeholder': 'shipping State',
        })
    ) 
     shipping_zipcode = forms.CharField(
        max_length=12, required=True, widget=forms.TextInput(attrs={
            'class': 'block w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-1 focus:ring-indigo-500',
            'placeholder': ' shipping Zipcode',
        })
    ) 
     shipping_country = forms.CharField(
        max_length=32, required=True, widget=forms.TextInput(attrs={
            'class': 'block w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-1 focus:ring-indigo-500',
            'placeholder': 'Shipping Country',
        })
    ) 
     
     class Meta:
         model=ShippingAddress
         fields=['shipping_full_name','shipping_phone','shipping_email', 'shipping_address1','shipping_address2','shipping_city','shipping_state','shipping_zipcode','shipping_state','shipping_country']
         exclude=['user']     


class PaymentForm(forms.Form):
     card_name=forms.CharField(
        max_length=40, required=True, widget=forms.TextInput(attrs={
            'class': 'block w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-1 focus:ring-indigo-500',
            'placeholder': 'CARD NAME',
        })
    )
     card_number=forms.CharField(
        max_length=25, required=True, widget=forms.TextInput(attrs={
            'class': 'block w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-1 focus:ring-indigo-500',
            'placeholder': ' CARD NUMBER',
        })
    )
     card_CVV=forms.CharField(
        max_length=12, required=True, widget=forms.TextInput(attrs={
            'class': 'block w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-1 focus:ring-indigo-500',
            'placeholder': 'CVV',
        })
    )
     card_exp_date=forms.CharField(
        max_length=20, required=True, widget=forms.TextInput(attrs={
            'class': 'block w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-1 focus:ring-indigo-500',
            'placeholder': 'EXPIRY DATE',
        })
    )