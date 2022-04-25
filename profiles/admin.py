from django.contrib import admin
from .models import UserProfile


class ProfileAdmin(admin.ModelAdmin):
    """ Profile Admin """

    readonly_fields = (
        'user',
        )

    fields = (
        'user',
        'default_phone_number',
        'default_street_address1',
        'default_street_address2',
        'default_town_or_city',
        'default_county',
        'default_postcode',
        'default_country',
    )

    list_display = (
        'user',
        'default_phone_number',
        'default_street_address1',
        'default_street_address2',
        'default_town_or_city',
        'default_county',
        'default_postcode',
        'default_country',
    )


admin.site.register(UserProfile)
