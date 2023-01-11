from django.contrib import admin
from .models import Category, Product

# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('gender', 'friendly_name', 'name',)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'image',)

    ordering = ('category',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
