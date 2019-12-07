from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [

    path('', views.homeView, name="home_url"),
    path('profile/', views.profileView, name="profile_url"),
    path('login/', views.loginView, name="login_url"),
    path('logout/', views.logoutView, name="logout_url"),
    path('loginjs/', views.loginJs),
    path('signupjs/', views.signupJs),
    path('username_check/', views.is_available),
    path('email_check/', views.email_is_available),
    path('profile_update/', views.profile_update),
    path('new_post/', views.new_post),
    path('new_comment/', views.new_Comment),
    path('delete_post/', views.post_delete),
    path('member/', views.member, name="member"),
    path('user/<slug>', views.others_profile, name="others_profile"),
    path('delte_comment/', views.delete_comment),


]
