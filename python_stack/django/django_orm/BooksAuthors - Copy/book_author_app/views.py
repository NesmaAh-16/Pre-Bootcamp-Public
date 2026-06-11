from django.shortcuts import render, redirect
from .models import Book, Author

# --- Book Views ---
def index(request):
    context = {
        "all_books": Book.objects.all()
    }
    return render(request, "index.html", context)

def add_book(request):
    Book.objects.create(
        title=request.POST['title'],
        desc=request.POST['desc']
    )
    return redirect('/')

def book_info(request, book_id):
    this_book = Book.objects.get(id=book_id)
    # SENSEI BONUS: Get authors NOT already associated with this book
    context = {
        "book": this_book,
        "not_associated_authors": Author.objects.exclude(books__id=book_id)
    }
    return render(request, "book_info.html", context)

def join_author(request):
    this_book = Book.objects.get(id=request.POST['book_id'])
    this_author = Author.objects.get(id=request.POST['author_id'])
    this_book.authors.add(this_author)
    return redirect(f"/books/{this_book.id}")

# --- Author Views ---
def authors(request):
    context = {
        "all_authors": Author.objects.all()
    }
    return render(request, "authors.html", context)

def add_author(request):
    Author.objects.create(
        first_name=request.POST['first_name'],
        last_name=request.POST['last_name'],
        notes=request.POST['notes']
    )
    return redirect('/authors')

def author_info(request, author_id):
    this_author = Author.objects.get(id=author_id)
    # SENSEI BONUS: Get books NOT already associated with this author
    context = {
        "author": this_author,
        "not_associated_books": Book.objects.exclude(authors__id=author_id)
    }
    return render(request, "author_info.html", context)

def join_book(request):
    this_author = Author.objects.get(id=request.POST['author_id'])
    this_book = Book.objects.get(id=request.POST['book_id'])
    this_author.books.add(this_book)
    return redirect(f"/authors/{this_author.id}")