from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.loginView, name="login_url"),
    path('logout/', views.logoutView, name="logout_url"),
    path('loginjs/', views.loginJs),
]
