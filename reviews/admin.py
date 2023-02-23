from django.contrib import admin
from .models import Review


class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'product',
        'user',
        'rating',
        'review',
        'date',
    )

    ordering = ('-date',)


admin.site.register(Review, ReviewAdmin)
