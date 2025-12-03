from django.contrib import admin
from django.urls import path
from accounts import views

urlpatterns = [
    path('login', views.SingUp.as_view(), name='singup'),
]