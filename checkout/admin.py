from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInLine(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInLine,)

    readonly_fields = ('order_number', 'date',
                       'product_total', 'delivery_cost',
                       'grand_total', 'original_bag', 'stripe_pid')

    fields = ('order_number', 'date', 'full_name', 'email', 'country',
              'city', 'address', 'product_total',
              'delivery_cost', 'grand_total', 'original_bag', 'stripe_pid')

    list_display = ('order_number', 'date', 'full_name', 'product_total',
                    'delivery_cost', 'grand_total',)

    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)
