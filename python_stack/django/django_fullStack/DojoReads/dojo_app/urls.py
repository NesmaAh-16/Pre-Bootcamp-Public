from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('login', views.login),
    path('logout', views.logout),
    path('books', views.books_home),
    path('books/add', views.add_book_page),
    path('books/create', views.create_book),
    path('books/<int:book_id>', views.show_book),
    path('books/<int:book_id>/review', views.create_review),
    path('reviews/<int:review_id>/delete', views.delete_review),
    path('users/<int:user_id>', views.show_user),
]