# import pytest
from django.conf import settings
import pytest

from django.contrib.auth.models import User, Group
from django.test import Client
from user.models import Employee

@pytest.fixture(scope='session')
def django_db_setup():
    settings.DATABASES['default'] = {
        'ENGINE': 'django.db.backends.postgres',
        'HOST': 'localhost',
        'NAME': 'postgres',
        'ATOMIC_REQUESTS': True,
}

@pytest.fixture
def new_user_factory(db):
    def create_app_user(
            username: str, 
            password: str = None, 
            first_name: str = 'firstname', 
            last_name: str = 'lastname',
            email: str = 'test@gmail.com', 
            is_staff: bool = False, 
            is_superuser: bool = False,
            group: Group = None,
            ): 
        user = User.objects.create_user(
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
            email=email,
            is_staff=is_staff,
            is_superuser=is_superuser
            )
        if group: 
            user.groups.add(group)
        return user
    return create_app_user

@pytest.fixture
def new_employee_factory(db):
    def create_app_employee(
            user: User = None,
            department: str = 'testepartment',
            phone: str = 'testphone',
            role: str = 'CO',
    ):
        employee = Employee.objects.create(
            user=user,
            department=department,
            phone=phone,
            role=role
        )
        return employee
    return create_app_employee

@pytest.fixture
def new_group_factory(db):
    def create_app_group(name: str = 'test_group'):
        group = Group.objects.create(name=name)
        return group
    return create_app_group
        

@pytest.fixture
def user1(db, new_user_factory):
    group = Group.objects.get(name='courier')
    return new_user_factory('test_user', 'test_password', 'test_name', group=group)

@pytest.fixture
def user2(db, new_user_factory):
    return new_user_factory('test_user_without_group', 'test_password', 'test_name')

        
@pytest.fixture
def employee1(db, user2, new_employee_factory):
    return new_employee_factory(user2)

@pytest.fixture
def employee2(db, user1, new_employee_factory):
    return new_employee_factory(user1)

@pytest.fixture
def client():
    return Client()