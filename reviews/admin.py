from django.contrib import admin
from .models import Review


class ReviewAdmin(admin.ModelAdmin):

    list_display = ('username', 'boat', 'score', 'created_on', 'updated_on')
    search_fields = ['username', 'boat']


admin.site.register(Review)
