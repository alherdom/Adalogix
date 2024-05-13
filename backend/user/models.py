from django.contrib.auth.models import User
from django.db import models


class Employee(models.Model):
    class EmployeeRole(models.TextChoices):
        STORE_ADMINISTRATOR = 'SA', 'Store Administrator'
        DELIVERY_EMPLOYEE = 'CO', 'Courier'
        STORE_SUPERADMINISTRATOR = 'SU', 'Store Super Administrator'

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=9, blank=True, null=True)
    role = models.CharField(max_length=2, choices=EmployeeRole.choices)
    available = models.BooleanField(default=True)
    route = models.TextField(blank=True, null=True)

    def is_store_admin(self):
        return self.role == 'SA'

    def is_delivery_employee(self):
        return self.role == 'CO'

    def is_store_superadmin(self):
        return self.role == 'SU'

    class meta:
        ordering = ['id']

class CustomUser(User):
    class Meta:
        proxy = True
        ordering = ['id']

    def __str__(self):
        return self.username

