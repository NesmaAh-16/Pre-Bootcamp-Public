from django.urls import path 
from . import views

urlpatterns = [
    path('',views.first),
    path('shows', views.index), #Displays table of all shows
    path('shows/new', views.new), #form to add new show
    path('shows/create', views.create), #adds to DB
    path('shows/<int:id>', views.show_info), #show page
    path('shows/<int:id>/edit', views.edit), #form to edit a show
    path('shows/<int:id>/update', views.update), #updates show in DB
    path('shows/<int:id>/destroy', views.destroy), #deletes show
]