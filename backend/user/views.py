from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpRequest, HttpResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth.models import Group


@csrf_exempt
@require_POST
def user_login(request: HttpRequest) -> HttpResponse:
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        if user.groups.filter(name='admin').exists():
            return HttpResponse('I\'m an admin')   
        if user.groups.filter(name='truckdriver').exists():
            return HttpResponse('I\'m a truckdriver')
    else:
        return HttpResponse(400)

@csrf_exempt
@require_POST
def user_logout(request: HttpRequest) -> HttpResponse:
    logout(request)
    return HttpResponse('logged out')

@csrf_exempt
@require_POST
def user_registration(request: HttpRequest) -> HttpResponse:
    if User.objects.filter(username = request.POST.get('username')):
        return HttpResponse('This username is already in use', status=400)
    username, password, email, first_name, last_name = request.POST.values()
    new_user = User.objects.create(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
    truckdriver_group = Group.objects.get(name='truckdriver')
    new_user.groups.add(truckdriver_group)
    return HttpResponse('Truckdriver created')





