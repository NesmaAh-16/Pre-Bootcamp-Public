from django.urls import path
from . import views


urlpatterns = [
    path('',views.books),
    path('create_book',views.create_book),
    path('show_book/<int:book_id>',views.book_details),
    path('join_author',views.join_authors),
    
    
    path('author',views.authors),
    path('create_author',views.create_author),
    path('show_author/<int:author_id>',views.author_details),
    path('join_book',views.join_books)
]