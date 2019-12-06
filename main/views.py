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
        if request.POST.get("is_img") == "True":
            try:
                profile = Profile.objects.get(id=request.POST.get("id"))
                if "default.png" not in str(profile.img):
                    profile.img.delete()
                profile.img = request.FILES['img']
                profile.save()
                return JsonResponse({"status": "200", "img_url": profile.img.url})
            except:
                return JsonResponse({"status": "404"})

        else:
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
            profile.name = f_name +" "+ l_name
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

    contact_list = Post.objects.order_by('-id').filter(user=request.user)
    paginator = Paginator(contact_list, 10)  # Show 10 contacts per page

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
            newPost.post = request.POST.get('post').strip()
            newPost.save()
            newPost.user.add(request.user)
            status = {
                'status': '200',
                'post_id': newPost.id
            }
        except:
            status = {'status': '404'}
    return JsonResponse(status)


@login_required
def new_Comment(request):
    if request.method == 'POST':
        try:
            newComment = Comment()
            newComment.comment = request.POST.get('comment').strip()
            newComment.username = request.user.username
            newComment.save()
            newComment.person.add(Profile.objects.get(
                user=request.user))
            post = Post.objects.get(id=request.POST.get('post_id'))
            post.comment.add(newComment)
            status = {'status': '200'}
        except Exception:
            raise
            status = {'status': '404'}
    return JsonResponse(status)


@login_required
def post_delete(request):
    if request.method == 'POST':
        try:
            post = Post.objects.get(pk=request.POST['pk'])
            for comment in post.comment.all():
                comment.delete()
            post.delete()
            status = {
                'status': '200',
            }
        except:
            status = {
                'status': '404',
            }
    return JsonResponse(status)

@login_required
def member(request):
    q =  request.GET.get('q')
    if q != None:
        members = Profile.objects.filter(name__icontains = q).exclude(user=request.user) | Profile.objects.filter(city__iexact = q).exclude(user=request.user) | Profile.objects.filter(blood__iexact = q).exclude(user=request.user)
        
    else:    
        member_list = Profile.objects.exclude(user=request.user)
        paginator = Paginator(member_list, 2)  # Show 10 contacts per page

        
        page = request.GET.get('page')
        members = paginator.get_page(page)
    return render(request,"main/members.html",{"members":members})

def others_profile(request,slug):
    user = User.objects.get(username=slug)
    profile = Profile.objects.get(user=user)

    contact_list = Post.objects.order_by('-id').filter(user=user)
    paginator = Paginator(contact_list, 10)  # Show 10 contacts per page

    page = request.GET.get('page')
    posts = paginator.get_page(page)
    context = {
        "user_info": user,
        "profile": profile,
        "posts":posts
    }
    return render(request,"main/others_profile.html",context)
