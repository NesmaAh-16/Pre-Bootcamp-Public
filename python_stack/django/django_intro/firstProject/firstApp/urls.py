from django.urls import path
from . import views

urlpatterns = [
    path('', views.root),
    path('blogs', views.index),
    path('blogs/news', views.new),
    path('blogs/create', views.create),
    path('blogs/<int:number>', views.show),#/blogs/7
    path('blogs/<int:number>/edit', views.edit),
    path('blogs/<int:number>/delete', views.destroy),
    path('blogs/json', views.json_res),#bonus
]
