import pytest
import json
from django.contrib.auth.models import User
def test_new_user(user1):
    print (user1.groups)
    assert user1.first_name == "test_name"

def test_new_employee(employee1):
    assert employee1.role == 'CO'
    assert employee1.is_delivery_employee()


@pytest.mark.parametrize(
        "username, firstName, lastName, email , password, role, validity, message",
        [
            ("dimas", "Dimas", "Abrante", "dimas@gmail.com", "1q2w3e4r", "CO", 200, ''),
            ("", "Dimas", "Abrante", "dimas@gmail.com", "1q2w3e4r", "CO", 400, b'You must fill all the fields'),
            ("dimas", "", "Abrante", "dimas@gmail.com", "1q2w3e4r", "CO", 400, b'You must fill all the fields'),
            ("dimas", "Dimas", "", "dimas@gmail.com", "1q2w3e4r", "CO", 400, b'You must fill all the fields'),
            ("dimas", "Dimas", "Abrante", "", "1q2w3e4r", "CO", 400, b'You must fill all the fields'),
            ("dimas", "Dimas", "Abrante", "dimas@gmail.com", "", "CO", 400, b'You must fill all the fields'),
            ("dimas", "Dimas", "Abrante", "dimas@gmail.com", "1q2w3e4r", "", 400, b'You must fill all the fields'),
            ("dimas", "Dimas", "Abrante", "dimas@gmail.com", "1q2w3e4r", "LA", 400, b'Invalid role'),
        ]
)


@pytest.mark.django_db
def test_user_registration(client, username, firstName, lastName, email, password, role, validity, message):
    response = client.post(
        path="/user/register/", 
        data=json.dumps({"username": username, "firstName": firstName, "lastName": lastName, "email": email, "password": password, "role": role}), 
        content_type="application/json"
        )
    assert response.status_code == validity
    if response.status_code != 200:
        assert response.content == message


@pytest.mark.parametrize(
        "user_name, password, validity",
        [
            ("test_user", "test_password", 200), 
            ("test_user", "wrong_password", 401),
            ("wrong_user", "test_password", 401),
            ("test_user_without_group", "test_password", 401)
        ]
)

@pytest.mark.django_db
def test_login(client, user1, user2, user_name, password, validity):
    response = client.post(path="/user/login/", data=json.dumps({"username": user_name, "password": password}), content_type="application/json")
    assert response.status_code == validity

def test_logout(client, user1):
    client.post(path="/user/login/", data=json.dumps({"username": "test_name", "password": "test_password"}), content_type="application/json")
    response = client.post("/user/logout/")
    assert response.status_code == 200


@pytest.mark.parametrize(
        "user_name, password, validity",
        [
            ("test_user", "test_password", 200),
        ]
)

def test_retrieve_employee_list(client, user1, user_name, password, validity):
    login_response = client.post(path="/user/login/", data=json.dumps({"username": user_name, "password": password}), content_type="application/json")
    headers = {"Authorization": f'Token {json.loads(login_response.content)["token"]}'}
    response = client.get(path="/user/list/", headers=headers)
    assert response.status_code == validity

@pytest.mark.parametrize(
        "user_name, password, validity",
        [
            ("test_user", "test_password", 200),
        ]
)

def test_retrieve_employee_detail(client, user1, employee1, user_name, password, validity):
    login_response = client.post(path="/user/login/", data=json.dumps({"username": user_name, "password": password}), content_type="application/json")
    headers = {"Authorization": f'Token {json.loads(login_response.content)["token"]}'}
    response = client.get(path=f"/user/detail/{employee1.id}/", headers=headers)
    assert response.status_code == validity
    assert json.loads(response.content)["username"] == employee1.user.username

@pytest.mark.parametrize(
        "user_name, password, validity",
        [
            ("test_user", "test_password", 204),
        ]
)

def test_delete_employee(client, user1, employee1, user_name, password, validity):
    from user.models import Employee
    login_response = client.post(path="/user/login/", data=json.dumps({"username": user_name, "password": password}), content_type="application/json")
    headers = {"Authorization": f'Token {json.loads(login_response.content)["token"]}'}
    employee_username = employee1.user.username
    response = client.delete(path=f"/user/delete/{employee1.id}/", headers=headers)
    assert response.status_code == validity
    assert Employee.objects.filter(user__username = employee_username).count() == 0

@pytest.mark.parametrize(
        "user_name, password, validity",
        [
            ("test_user", "test_password", 200),
        ]
)

def test_multiple_delete_employee(client, user1, employee1, employee2, user_name, password, validity):
    from user.models import Employee
    login_response = client.post(path="/user/login/", data=json.dumps({"username": user_name, "password": password}), content_type="application/json")
    headers = {"Authorization": f'Token {json.loads(login_response.content)["token"]}'}
    # TODO: Check the use of the user id as the id we use to delete employees
    data = json.dumps({"employee_ids": [employee1.user.id, employee2.user.id]})
    employee1_username = employee1.user.username
    employee2_username = employee2.user.username
    response = client.delete(path="/user/delete/multiple/", headers=headers, data=data)
    assert response.status_code == validity
    assert Employee.objects.filter(user__username = employee1_username).count() == 0
    assert Employee.objects.filter(user__username = employee2_username).count() == 0
    
@pytest.mark.parametrize(
        "user_name, password, field_to_change, new_value,  validity",
        [
            ("test_user", "test_password", "username", "new_username", 200),
            ("test_user", "test_password", "first_name", "new_first_name", 200),
            ("test_user", "test_password", "last_name", "new_last_name", 200),
            ("test_user", "test_password", "email", "new_email", 200),
            ("test_user", "test_password", "role", "CO", 200),
            ("test_user", "test_password", "role", "SA", 200),
            ("test_user", "test_password", "department", "new_department", 200),
            ("test_user", "test_password", "phone", "123456789", 200),
        ]
)

def test_employee_update(client, user1, employee1, user_name, password, field_to_change, new_value,  validity):
    login_response = client.post(path="/user/login/", data=json.dumps({"username": user_name, "password": password}), content_type="application/json")
    headers = {"Authorization": f'Token {json.loads(login_response.content)["token"]}', "Content-Type": "application/json"}
    data = {field_to_change: new_value}
    response = client.patch(path=f"/user/update/{employee1.id}/", data=data, headers=headers, content_type="application/json")
    assert response.status_code == validity
    if field_to_change == 'role':
        new_value = 'courier' if new_value == 'CO' else 'admin'
    assert json.loads(response.content)[field_to_change] == new_value



