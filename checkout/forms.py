from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('full_name', 'email', 'country',
                  'city', 'address', 'postcode',)

    def __init__(self, *args, **kwargs):
        """Adds placeholders and classes, removes auto-generated labels
        and set focus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {'full_name': 'Fullname',
                        'email': 'Email Address',
                        'country': 'Country',
                        'city': 'City',
                        'address': 'Address',
                        'postcode': 'Postcode',
                        }

        self.fields['full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholder[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False
