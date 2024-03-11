import pytest
from django.contrib.auth.models import User
from user.models import Employee


@pytest.fixture
def user():
    return User.objects.create(username='usertest', password='usertest')


@pytest.fixture
def delivery_employee(
    user, role: str = 'DE', phone: str = '666666666', department: str = 'Test department'
):
    return Employee.objects.create(user=user, role=role, phone=phone, department=department)


@pytest.fixture
def store_admin_employee(
    user, role: str = 'SA', phone: str = '666666666', department: str = 'Test department'
):
    return Employee.objects.create(user=user, role=role, phone=phone, department=department)


@pytest.mark.django_db
def test_store_admin_employee_creation(store_admin_employee, user):
    employee = store_admin_employee
    assert employee.user == user
    assert employee.role == 'SA'
    assert employee.phone == '666666666'
    assert employee.department == 'Test department'
    assert employee.is_store_admin()


@pytest.mark.django_db
def test_delivery_employee_creation(delivery_employee):
    employee = delivery_employee
    assert employee.role == 'DE'
    assert employee.is_delivery_employee()
