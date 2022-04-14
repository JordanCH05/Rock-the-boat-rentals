from django.contrib import admin
from .models import Category, Boat


@admin.register(Boat)
class BoatAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'manufacturer',
        'year_built',
        'location',
        'fuel',
        'condition',
        'image',
        'length',
    )
    list_filter = (
        ('image', admin.BooleanFieldListFilter),
        'category',
        'currency',
        )

    search_fields = [
        'sku',
        'manufacturer',
        'year_built',
        'location',
        'fuel',
        'condition',
        ]

    ordering = ('sku',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )
