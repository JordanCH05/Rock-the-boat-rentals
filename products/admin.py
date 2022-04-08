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
    )

    ordering = ('sku',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )
