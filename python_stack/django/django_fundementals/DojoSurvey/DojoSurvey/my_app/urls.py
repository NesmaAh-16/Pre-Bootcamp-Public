from django.urls import path 
from . import views

urlpatterns = [
    path('', views.index),
    path('createUser', views.create_user), #process the form
    path('result', views.result_user),     #result of the form
]
