from django.contrib import admin
from .models import Customer


"""  Customer Admin  """


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('customer_id', 'full_name', 'email',)
