from django.contrib import admin
from .models import Category, Boat


@admin.register(Boat)
class BoatAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'currency',
        'price',
        'brand',
        'state_of_assembly',
        'power_source',
        'age_range',
        'length',
        'width',
        'height',
        'speed',
        'material',
        'views',
    )
    list_filter = (
        ('image', admin.BooleanFieldListFilter),
        'category',
        'currency',
        )

    search_fields = [
        'sku',
        'name',
        'brand',
        'state_of_assembly',
        'power_source',
        'material',
        ]

    ordering = ('name',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )
