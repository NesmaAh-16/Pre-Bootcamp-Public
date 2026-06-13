from django.urls import path
from . import views 


urlpatterns = [
    path('', views.index),
    path('create_course',views.create_course),
    path('courses/destroy/<int:id>',views.remove),
    path('courses/<int:id>/destroy', views.destroy), 
    path('courses/comments/<int:id>', views.comments)
]