import csv

from django.core.management import BaseCommand

from store.models import Store


class Command(BaseCommand):
    help = 'Load the datababase with some info about users'

    def handle(self, *args, **kwargs):
        with open('store/management/data/stores.csv', 'r') as file:
            f = csv.DictReader(file)
            for line in f:
                Store.objects.create(
                    name=line['name'],
                    address=line['address'],
                    capacity=line['capacity'],
                    latitude=line['latitude'],
                    longitude=line['longitude'],
                )
