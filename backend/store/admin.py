from django.contrib import admin

from .models import Store


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'capacity', 'address']
    list_display_links = ['id', 'name']
    search_fields = ['name', 'capacity', 'address']
