from django import forms
from .models import Product, Category, Review

from crispy_forms.bootstrap import Field
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Div, Fieldset


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-1'


class ReviewForm(forms.ModelForm):
    """Enable users to leave comments for products"""
    class Meta:
        model = Review
        fields = ('rating', 'review')

    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)
        # create form structure using crispy forms
        self.helper = FormHelper()
        self.helper.form_id = 'product-review-form'
        self.helper.form_method = 'post'
        self.helper.form_class = 'mt-4'
        self.helper.add_input(
            Submit('submit', 'Add Review', css_class='btn btn-primary \
            float-right'))
        self.helper.layout = Layout(
            Fieldset('Add a product review',
                     Div(
                         Field('rating', wrapper_class='col-12 col-md-2'),
                         Field(
                             'review', wrapper_class='col-12 col-md-10',
                             rows=5, placeholder="Add your review here"),
                         css_class='row')
                     )
        )
