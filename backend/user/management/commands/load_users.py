from django.contrib.auth.models import Group, User
from django.core.management import BaseCommand

from user.models import Employee


class Command(BaseCommand):
    help = 'Load the datababase with some info about users'

    def handle(self, *args, **kwargs):
        # First we create an admin
        User.objects.create_superuser(username='admin', email='admin@admin.com', password='12345')
        # Courier users
        new_user = User(
            username='antoniodriver',
            email='antonio@gmail.com',
            first_name='Antonio',
            last_name='Gómez',
        )
        new_user.set_password('12345HOLA')
        new_user.save()
        Employee.objects.create(user=new_user, role='CO')
        truckdriver_group = Group.objects.get(name='courier')
        new_user.groups.add(truckdriver_group)

        new_user2 = User(
            username='juandriver',
            email='juan@gmail.com',
            first_name='Juan',
            last_name='Llanos',
        )
        new_user2.set_password('12345HOLA')
        new_user2.save()
        Employee.objects.create(user=new_user2, role='CO')
        truckdriver_group = Group.objects.get(name='courier')
        new_user2.groups.add(truckdriver_group)

        new_user3 = User(
            username='sergiodriver',
            email='sergio@gmail.com',
            first_name='Sergio',
            last_name='Gómez',
        )
        new_user3.set_password('12345HOLA')
        new_user3.save()
        Employee.objects.create(user=new_user3, role='CO')
        truckdriver_group = Group.objects.get(name='courier')
        new_user3.groups.add(truckdriver_group)
        # Admin user
        new_admin = User(
            username='manueladmin', email='manuel@gmail.com', first_name='Manuel', last_name='López'
        )
        new_admin.set_password('12345HOLA')
        new_admin.save()
        admin_group = Group.objects.get(name='admin')
        new_admin.groups.add(admin_group)
        Employee.objects.create(user=new_admin, role='SA')
