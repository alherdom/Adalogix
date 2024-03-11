import pytest
from django.contrib.auth.models import User

from user.models import Employee


@pytest.mark.django_db
def test_store_admin_employee_creation():
    user = User(username='usertest', password='usertest')
    employee = Employee(user=user, role='SA', phone='666666666', department='Department test')
    last_id = User.objects.latest('id')
    assert employee.id == last_id + 1
    assert employee.user == user
    assert employee.role == 'SA'
    assert employee.phone == '666666666'
    assert employee.department == 'Department test'
