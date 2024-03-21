from django.db import models


class Store(models.Model):
    adress = models.CharField(max_length=255)
    capacity = models.PositiveIntegerField()
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name

    def can_add_products(self, amout: int) -> bool:
        return self.capacity - amout >= 0
