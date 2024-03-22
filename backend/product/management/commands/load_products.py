import csv
from random import randint

from django.core.management import BaseCommand

from product.models import Product
from store.models import Store


class Command(BaseCommand):
    help = 'Load the datababase with some info about users'

    def handle(self, *args, **kwargs):
        with open('product/management/data/products.csv', 'r') as file:
            f = csv.DictReader(file)
            for index, line in enumerate(f):
                prod = Product.objects.create(
                    name=line['name'],
                    description=line['description'],
                    price=line['price'],
                    weight=line['weight'],
                    volume=line['volume'],
                )
                store1 = Store.objects.get(id=randint(1, 10))
                store2 = Store.objects.get(id=randint(1, 10))
                prod.stores.add(store1, through_defaults={'stock': randint(10, 50)})
                prod.stores.add(store2, through_defaults={'stock': randint(10, 50)})
                prod.save()
