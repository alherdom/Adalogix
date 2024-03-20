from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
import json

@csrf_exempt
@require_POST
def user_login(request: HttpRequest) -> HttpResponse:
    data = json.loads(request.body)
    username = data['username']
    password = data['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        user_object = User.objects.get(username=user)
        if not user_object.groups.all():
            return HttpResponse('This user has no group',status=400)
        if user.groups.filter(name='admin').exists():
            return JsonResponse(dict(id=user_object.id, group="admin", status=200, message="Admin successfully logged in"))   
        if user.groups.filter(name='truckdriver').exists():
            return JsonResponse(dict(id=user_object.id, group="truckdriver", status=200, message="Truckdriver successfully logged in"))
    else:
        return HttpResponse(status=400)

@csrf_exempt
@require_POST
def user_logout(request: HttpRequest) -> HttpResponse:
    logout(request)
    return HttpResponse('logged out')

@csrf_exempt
@require_POST
def user_registration(request: HttpRequest) -> HttpResponse:
    data = json.loads(request.body)
    username, password, email, first_name, last_name = data['username'], data['password'], data['email'], data['first_name'], data['last_name']
    if not all([username, email, first_name, last_name, password]):
        return HttpResponse('You must fill all the fields', status=400)
    if User.objects.filter(username = data['username']):
        return HttpResponse('This username is already in use', status=400)
    new_user = User(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
    new_user.set_password(password)
    new_user.save()
    truckdriver_group = Group.objects.get(name='truckdriver')
    new_user.groups.add(truckdriver_group)
    return JsonResponse(dict(username=new_user.username,id=new_user.id, status=200, message="User successfully registered"))





