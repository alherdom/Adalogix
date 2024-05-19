from django.db import models

from store.models import Store


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=9, decimal_places=2)
    category = models.CharField(max_length=255)
    weight = models.DecimalField(max_digits=7, decimal_places=2)
    volume = models.DecimalField(max_digits=7, decimal_places=2)
    stores = models.ManyToManyField(Store, through='Inventory', blank=True)

    def __str__(self) -> str:
        return f'{self.name}-{self.pk}'

    class Meta:
        ordering = ['id']


class Inventory(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    stock = models.PositiveIntegerField()
