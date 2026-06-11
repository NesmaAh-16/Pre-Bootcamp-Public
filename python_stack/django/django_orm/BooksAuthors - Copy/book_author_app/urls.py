from django.urls import path
from . import views

urlpatterns = [
    # Book routes
    path('', views.index), # Page to view all books and add one
    path('add_book', views.add_book),
    path('books/<int:book_id>', views.book_info), # Specific book details
    path('join_author', views.join_author), # Associate author to book

    # Author routes
    path('authors', views.authors), # Page to view all authors and add one
    path('add_author', views.add_author),
    path('authors/<int:author_id>', views.author_info), # Specific author details
    path('join_book', views.join_book), # Associate book to author
]