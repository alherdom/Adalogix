import json
from django.contrib.auth import authenticate, logout
from django.contrib.auth.models import Group, User
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, UpdateAPIView, RetrieveAPIView, DestroyAPIView
from .serializers import EmployeeSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticated
from .utils import password_generator, send_registration_email, send_reset_password_email
from .models import Employee
from django.shortcuts import get_object_or_404


class LoginView(APIView):
    authentication_classes = [TokenAuthentication]

    def post(self, request):
        data = json.loads(request.body)
        user = authenticate(username=data['username'], password=data['password'])
        if user:
            user = User.objects.get(username=data['username'])
            if token_existance := Token.objects.filter(user=user):
                token_existance[0].delete()
            token, created = Token.objects.get_or_create(user=user)
            if user.groups.filter(name='admin').exists():
                group = 'admin'
            elif user.groups.filter(name='courier').exists():
                group = 'courier'
            else:
                return JsonResponse({'error': 'User has no role'}, status=401)
            return JsonResponse(
                dict(
                    id=user.employee.id,
                    user=user.id,
                    name=user.get_full_name(),
                    group=group,
                    status=200,
                    message='Admin successfully logged in',
                    token=token.key,
                )
            )
        else:
            return JsonResponse({'error': 'Invalid credentials'}, status=401)


@csrf_exempt
@require_POST
def user_logout(request: HttpRequest) -> HttpResponse:
    logout(request)
    return HttpResponse('logged out')


@csrf_exempt
@require_POST
def user_registration(request: HttpRequest) -> HttpResponse:
    data = json.loads(request.body)
    username, email, first_name, last_name, role = (
        data['username'],
        data['email'],
        data['firstName'],
        data['lastName'],
        data['role'],
    )
    if not all([username, email, first_name, last_name, role]):
        return HttpResponse('You must fill all the fields', status=400)
    if User.objects.filter(username=username):
        return HttpResponse('This username is already in use', status=400)
    if role not in list(Employee.EmployeeRole):
        return HttpResponse('Invalid role', status=400)

    password = password_generator()
    new_user = User.objects.create_user(
        username=username,
        email=email,
        password=password,
        first_name=first_name,
        last_name=last_name,
    )
    Employee.objects.create(user=new_user, role=role)
    employee_group = (
        Group.objects.get(name='admin') if role == 'SA' else Group.objects.get(name='courier')
    )
    new_user.groups.add(employee_group)
    send_registration_email(first_name, last_name, email, username, password)

    return JsonResponse(
        dict(
            username=new_user.username,
            id=new_user.id,
            status=200,
            message='User successfully registered, email sent with credentials',
        )
    )


def get_user_id_by_employee_id(employee_id):
    employee = get_object_or_404(Employee, id=employee_id)
    return employee.user.id


@csrf_exempt
@require_POST
def reset_password(request: HttpRequest) -> HttpResponse:
    data = json.loads(request.body)
    userId = get_user_id_by_employee_id(data['employeeId'])
    if not User.objects.filter(id=userId):
        return JsonResponse({'error': 'User not found'}, status=404)
    user = User.objects.get(id=userId)
    password = password_generator()
    user.set_password(password)
    user.save()
    send_reset_password_email(user.first_name, user.last_name, user.email, user.username, password)
    return JsonResponse({'status': 200, 'message': 'Password reset email sent'})


class EmployeeListView(ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class AvailableEmployeeListView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = EmployeeSerializer

    def get_queryset(self):
        queryset = Employee.objects.filter(available=True, role='CO')
        return queryset


class EmployeeUpdateView(UpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def patch(self, request, *args, **kwargs):
        partial = True
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return JsonResponse(dict(status=200, message='Employee successfully updated'))


# TODO: Review how to update the employee model and the user model at the same time. We have a problem with the to_representation function.


class EmployeeDetailView(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class UserDeleteView(DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return JsonResponse({'status': 200})


class UserMultipleDelete(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request):
        data = json.loads(request.body)
        employee_ids = data['employee_ids']
        for employee_id in employee_ids:
            User.objects.get(id=employee_id).delete()
        return JsonResponse({'status': 200})
