from django.db import models

from product.models import Product
from store.models import Store


class Inventory(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    stock = models.PositiveIntegerField()
