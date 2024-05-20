from django.db import models
from store.models import Store
from user.models import Employee
from product.models import Product
from .validators import validate_quantity

class Order(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='orders')
    courier = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='orders', blank=True, null=True)
    products = models.ManyToManyField(Product, through='OrderProduct')
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    completion_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f'Order_{self.pk}'
    
class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveBigIntegerField(default=1)

    def clean(self) -> None:
        validate_quantity(self.quantity, self.product, self.order)

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)