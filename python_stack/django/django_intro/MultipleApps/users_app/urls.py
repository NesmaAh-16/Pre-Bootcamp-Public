from django.urls import path
from . import views

urlpatterns = [
    path('register', views.register),
    path('login', views.login),
    path('users/new', views.register), # Reusing the register method
    path('users', views.index),
]