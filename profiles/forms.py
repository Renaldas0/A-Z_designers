from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        """Adds placeholders and classes, removes auto-generated labels
        and set focus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {'default_city': 'City',
                        'default_address': 'Address',
                        'default_postcode': 'Postcode',
                        }

        self.fields['default_city'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'default_country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
                self.fields[field].widget.attrs['class'] = 'border-black rounded-1 profile-form-input'
                self.fields[field].label = False
