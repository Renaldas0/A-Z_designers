from django.contrib import admin
from .models import DiscountCode


class DiscountCodeAdmin(admin.ModelAdmin):
    list_display = ('code', 'valid_for_first_purchase', 'discount_percentage')


admin.site.register(DiscountCode, DiscountCodeAdmin)
