from django.contrib import admin
from .models import Category, Product

# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('gender', 'friendly_name', 'name',)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('sku', 'name', 'category', 'description', 'price', 'image',)

    ordering = ('sku',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
