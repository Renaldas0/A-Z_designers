from django.contrib import admin
from .models import Category, Product, Review

# Register your models here.


class ReviewInline(admin.TabularInline):
    """Tabular Inline View for Product Reviews"""
    model = Review


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('gender', 'friendly_name', 'name',)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('sku', 'name', 'category', 'description', 'key_words',
                    'price', 'image',)

    ordering = ('sku',)

    inlines = [
        ReviewInline,
    ]


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
