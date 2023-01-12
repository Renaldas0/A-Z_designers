"""Imports"""
from django import forms
from djando.conf import settings
from .models import Customer


class CustomerForm(forms.ModelForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = Customer
        fields = ('full_name', 'email',)
