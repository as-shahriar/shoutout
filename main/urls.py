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
]
