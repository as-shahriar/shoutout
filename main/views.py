from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import JsonResponse


def loginJs(request):
    username = request.POST.get('username')
    password = request.POST.get('password')

    user = authenticate(username=username, password=password)
    if user is None:
        try:
            obj = User.objects.get(email=username)
            user = authenticate(username=obj.username, password=password)
        except:
            status = "404"
    if user is not None:
        login(request, user)
        status = "200"

    data = {
        'status': status
    }
    return JsonResponse(data)


def loginView(request):
    return render(request, 'main/index.html')


def logoutView(request):
    logout(request)
    return redirect('login_url')
