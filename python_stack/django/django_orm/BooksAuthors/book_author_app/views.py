from django.shortcuts import render , redirect
from .models import *


def books(request):
    context={
        "all_books":Book.objects.all()
    }
    return render(request, "book.html" , context)

def create_book(request):
    if request.method =='POST':
        Book.objects.create(
            title = request.POST['title'],
            desc = request.POST['desc']
        )
    return redirect('/')

def book_details(request,book_id):
    this_book=Book.objects.get(id=book_id)
    context = {
        "book": this_book,
        "not_associated_authors":Author.objects.exclude(books__id=book_id)
        
    }
    return render(request, "book_details.html",context)

def join_authors(request):
    this_book = Book.objects.get(id=request.POST['book_id'])
    this_author = Author.objects.get(id=request.POST['author_id'])
    this_book.authors.add(this_author)
    return redirect(f'show_book/{this_book.id}')



def authors(request):
    context={
        "all_authors":Author.objects.all()
    }
    return render(request, "author.html" , context)

def create_author(request):
    if request.method =='POST':
        Author.objects.create(
            first_name = request.POST['first_name'],
            last_name = request.POST['last_name'],
            notes = request.POST['notes']
        )
    return redirect('/author')

def author_details(request,author_id):
    this_author=Author.objects.get(id=author_id)
    context = {
        "author": this_author,
        "not_associated_books":Book.objects.exclude(authors__id=author_id)
    }
    return render(request, "author_details.html",context)

def join_books(request):
    this_author = Author.objects.get(id=request.POST['author_id'])
    this_book = Book.objects.get(id=request.POST['book_id'])
    this_author.books.add(this_book)
    return redirect(f'show_author/{this_author.id}')