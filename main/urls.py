from django.urls import path
from django.contrib.auth import views
from . import views 


urlpatterns = [
    path("", views.home, name= 'home'),   
    path('vestibular', views.vestibular, name ='vestibular'),
]

