from django.contrib.auth.models import Group, User
from django.core.management import BaseCommand


class Command(BaseCommand):
    help = 'Load the datababase with some info about users'

    def handle(self, *args, **kwargs):
        # First we create an admin
        User.objects.create_superuser(username='admin', email='admin@admin.com', password='12345')
        # Truckdriver user
        new_user = User(
            username='User1', email='test@gmail.com', first_name='Pepe', last_name='Pepe'
        )
        new_user.set_password('12345HOLA')
        new_user.save()
        truckdriver_group = Group.objects.get(name='truckdriver')
        new_user.groups.add(truckdriver_group)
        # Admin user
        new_admin = User(
            username='User2', email='test@gmail.com', first_name='Pepe', last_name='Pepe'
        )
        new_admin.set_password('12345HOLA')
        new_admin.save()
        admin_group = Group.objects.get(name='admin')
        new_admin.groups.add(admin_group)
