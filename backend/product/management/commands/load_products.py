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
                store_first_id = Store.objects.all().order_by('id').first().id
                store_last_id = Store.objects.all().order_by('-id').first().id
                store1 = Store.objects.get(id=randint(store_first_id, store_last_id))
                store2 = Store.objects.get(id=randint(store_first_id, store_last_id))
                prod.stores.add(store1, through_defaults={'stock': randint(10, 50)})
                prod.stores.add(store2, through_defaults={'stock': randint(10, 50)})
                prod.save()
