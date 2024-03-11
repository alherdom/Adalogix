import pytest
from django.contrib.auth.models import User
from user.models import Employee


@pytest.mark.django_db
def test_store_admin_employee_creation():
    user = User(username='usertest', password='usertest')
    employee = Employee(user=user, role='SA', phone='666666666', department='Department test')
    assert employee.user == user
    assert employee.role == 'SA'
    assert employee.phone == '666666666'
    assert employee.department == 'Department test'


@pytest.mark.django_db
def test_delivery_employee_creation():
    user = User(username='usertest', password='usertest')
    employee = Employee(user=user, role='DE', phone='666666666', department='Department test')
    assert employee.user == user
    assert employee.role == 'DE'
    assert employee.phone == '666666666'
    assert employee.department == 'Department test'


@pytest.mark.django_db
def test_id_correcly_generated():
    user = User.objects.create(username='usertest', password='usertest')
    last_id = Employee.objects.latest('id').id
    employee = Employee.objects.create(
        user=user, role='DE', phone='666666666', department='Department test'
    )
    assert employee.id == last_id + 1
