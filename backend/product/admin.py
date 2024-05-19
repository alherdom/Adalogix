from django.contrib import admin

from .models import Inventory, Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'description', 'price', 'weight', 'volume',]


@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'product', 'store', 'stock']
