from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
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


def signupJs(request):
    status = "404"
    if request.method == "POST":
        fname = request.POST.get('fname').strip().title()
        lname = request.POST.get('lname').strip().title()
        username = request.POST.get('username').lower().strip()
        email = request.POST.get('email').strip().lower()
        password = request.POST.get('pwd')

        if fname != "" and lname != "" and username != "" and email != "" and password != "":
            if (User.objects.filter(email__iexact=email).count()) != 0 or (User.objects.filter(username__iexact=username).count()) != 0:
                return JsonResponse({'status': "404"})

            user = User()
            user.first_name = fname
            user.last_name = lname
            user.username = username
            user.email = email
            user.set_password(password)
            user.save()
            status = "200"

    data = {
        'status': status
    }

    return JsonResponse(data)


@login_required
def homeView(request):
    return render(request, 'main/home.html')


@login_required
def profileView(request):
    return render(request, 'main/profile.html')


def loginView(request):
    return render(request, 'main/index.html')


def logoutView(request):
    logout(request)
    return redirect('login_url')
