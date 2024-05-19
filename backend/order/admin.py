from django.contrib import admin
from order.models import Order, OrderProduct

class OrderProductInline(admin.TabularInline):
    model = OrderProduct
    extra = 1

@admin.register(Order)
class EmployeeAdmin(admin.ModelAdmin):
    inlines = [OrderProductInline]
    list_display = ('id', 'store', 'courier', 'created_at')

