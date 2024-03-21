from django.db import models

from inventory.models import Inventory
from store.models import Store


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=9, decimal_places=2)
    weight = models.DecimalField(max_digits=7, decimal_places=2)
    volume = models.DecimalField(max_digits=7, decimal_places=2)
    stores = models.ManyToManyField(Store, through=Inventory)
