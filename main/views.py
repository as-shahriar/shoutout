from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Profile, Post, Comment
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.core.paginator import Paginator


def is_available(request):
    username = request.GET.get('username').lower().strip()
    for _ in username:
        if _ == " ":
            return JsonResponse({'status': '404'})
    if User.objects.filter(username__iexact=username).count() != 0:
        return JsonResponse({'status': '404'})
    else:
        return JsonResponse({'status': '200'})


def email_is_available(request):
    email = request.GET.get('email').lower().strip()
    print(len(email))
    if User.objects.get(username=request.user).email == email:
        return JsonResponse({'status': '200'})
    elif len(email) == 0 or User.objects.filter(email__iexact=email).count() != 0:
        return JsonResponse({'status': '404'})
    else:
        return JsonResponse({'status': '200'})


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

        for _ in username:
            if _ == " ":
                return JsonResponse({'status': '404'})

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
            print(request.user)
            login(request, user)
            status = "200"

    data = {
        'status': status
    }

    return JsonResponse(data)


@login_required
def profile_update(request):
    is_changed = False
    if request.method == "POST":
        f_name = request.POST.get('f_name').strip().title()
        l_name = request.POST.get('l_name').strip().title()
        profession = request.POST.get('profession').strip().title()
        city = request.POST.get('city').strip().title()
        cell = request.POST.get('cell').strip()
        email = request.POST.get('email').lower().strip()
        blood = request.POST.get('blood').strip()
        gender = request.POST.get('gender').strip().title()

        user = User.objects.get(username=request.user)
        if user.first_name != f_name:
            user.first_name = f_name
            is_changed = True
        if user.last_name != l_name:
            user.last_name = l_name
            is_changed = True
        if user.email != email and (User.objects.filter(email__iexact=email).count()) == 0 and len(email) != 0:
            user.email = email
            is_changed = True

        profile = Profile.objects.get(user=request.user)
        profile.city = city
        profile.gender = gender
        profile.profession = profession
        profile.cell = cell
        profile.blood = blood
        profile.save()

        if is_changed:
            user.save()
        return JsonResponse({'status': '200'})


@login_required
def homeView(request):
    return render(request, 'main/home.html')


@login_required
def profileView(request):
    try:
        user_profile = Profile.objects.get(user=request.user)
    except:
        user_profile = Profile(user=request.user)
        user_profile.save()

    # for i in range(40):
    #     u = Post()
    #     u.post = "This is post"+str(i+1)
    #     u.save()
    #     u.user.add(request.user)

    contact_list = Post.objects.order_by('-id').filter(user=request.user)
    paginator = Paginator(contact_list, 10)  # Show 25 contacts per page

    page = request.GET.get('page')
    posts = paginator.get_page(page)

    context = {
        'user_profile': user_profile,
        'posts': posts,
    }

    return render(request, 'main/profile.html', context)


def loginView(request):
    return render(request, 'main/index.html')


def logoutView(request):
    logout(request)
    return redirect('login_url')


@login_required
def new_post(request):
    if request.method == 'POST':
        try:
            newPost = Post()
            newPost.post = request.POST.get('post')
            newPost.save()
            newPost.user.add(request.user)
            status = {'status': '200'}
        except:
            status = {'status': '404'}
    return JsonResponse(status)
