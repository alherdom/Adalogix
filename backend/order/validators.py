from django.core.exceptions import ValidationError
from product.models import Inventory

def validate_quantity(value, product, order):
    if int(value) < 0:
        raise ValidationError('Quantity cannot be less than 0')
    if int(value) > Inventory.objects.get(product=product, store=order.store).stock:
        raise ValidationError('Quantity cannot be greater than the available stock')