from django.contrib import admin
from .models import Employee, CustomUser


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'department', 'phone', 'role', 'available', 'route')
    search_fields = ('id', 'user__username', 'user__first_name', 'user__last_name', 'department')

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'first_name', 'last_name', 'email')
    search_fields = ('id', 'username', 'first_name', 'last_name')