from django.shortcuts import render
from django.contrib.auth import authenticate, login
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
def truckdriver_registration(request: HttpRequest) -> HttpResponse:
    username = request.POST.get('username')
    password = request.POST.get('password')
    email = request.POST.get('email')
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    new_user = User.objects.create(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
    new_user.groups.add(Group.objects.get('truckdriver'))
    new_user.save()
    return HttpResponse('Truckdriver created')

    