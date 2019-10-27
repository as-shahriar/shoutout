from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages


def loginView(request):
    if request.method == 'POST' and 'Login' in request.POST:
        username_or_email = request.POST.get('user_email')
        password = request.POST.get('user_password')
        user = authenticate(username=username_or_email, password=password)
        if user is None:
            try:
                obj = User.objects.get(email=username_or_email)
                user = authenticate(username=obj.username, password=password)
            except:
                messages.error(request, "Error")
        if user is not None:
            login(request, user)
            print("##############LOGIN#################")
            return redirect('login_url')
    elif request.method == 'POST' and 'register' in request.POST:
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('pwd')

        try:
            user = User()
            user.first_name = fname
            user.last_name = lname
            user.username = username
            user.email = email
            user.password = password
            user.save()
        except:
            raise
    return render(request, 'main/index.html')
