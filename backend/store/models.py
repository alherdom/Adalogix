from django.db import models


class Store(models.Model):
    address = models.CharField(max_length=255)
    capacity = models.PositiveIntegerField()
    name = models.CharField(max_length=255)
    longitude = models.DecimalField(max_digits=18, decimal_places=15, blank=True, null=True)
    latitude = models.DecimalField(max_digits=18, decimal_places=15, blank=True, null=True)

    def __str__(self) -> str:
        return self.name

    def can_add_products(self, amout: int) -> bool:
        return self.capacity - amout >= 0
