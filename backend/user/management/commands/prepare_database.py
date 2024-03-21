from django.contrib.auth.models import Group
from django.core.management import BaseCommand, call_command


class Command(BaseCommand):
    help = 'Start the database of the project with some data'

    def handle(self, *args, **kwargs):
        call_command('migrate')
        Group.objects.get_or_create(name='truckdriver')
        Group.objects.get_or_create(name='admin')
        call_command('load_users')
