from django.contrib import admin


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    """  Customer Admin  """
    list_display = ('customer_id', 'full_name', 'email',)
