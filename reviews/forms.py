from django import forms
from .models import Review
from products.models import Category, Product
from django.contrib.auth.models import User


class ReviewForm(forms.ModelForm):
    # Create a form that works with the Review model

    class Meta:
        model = Review
        fields = 'review','rating',

    review = forms.CharField(widget=forms.Textarea)
    rating = forms.ChoiceField(choices=[(i, i) for i in range(1, 6)],
                               widget=forms.RadioSelect)
