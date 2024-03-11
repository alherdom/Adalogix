from django.contrib.auth.models import User
from django.db import models


class Employee(models.Model):
    class EmployeeRole(models.TextChoices):
        STORE_ADMINISTRATOR = 'SA', 'Store Administrator'
        DELIVERY_EMPLOYEE = 'DE', 'Delivery Man'

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.CharField(max_length=255)
    phone = models.IntegerField(max_length=9)
    role = models.CharField(max_lengt=2, choices=EmployeeRole)

    def is_store_admin(self):
        return self.role == 'SA'

    def is_delivery_employee(self):
        return self.role == 'DE'
