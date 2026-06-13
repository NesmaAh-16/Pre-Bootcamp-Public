from django.shortcuts import render, redirect
from .models import Book, Author


def index(request):
    return redirect("/books")


def books_index(request):
    context = {"all_books": Book.objects.all()}
    return render(request, "books.html", context)


def create_book(request):
    if request.method == "POST":
        Book.objects.create(
            title=request.POST["title"], desc=request.POST["description"]
        )
    return redirect("/books")


def view_book(request, book_id):
    current_book = Book.objects.get(id=book_id)
    context = {
        "book": current_book,
        "available_authors": Author.objects.exclude(books=current_book),
    }
    return render(request, "view_book.html", context)


def add_author_to_book(request, book_id):
    if request.method == "POST":
        book_instance = Book.objects.get(id=book_id)
        author_instance = Author.objects.get(id=request.POST["author_id"])
        book_instance.authors.add(author_instance)
    return redirect(f"/books/{book_id}")


def authors_index(request):
    context = {"all_authors": Author.objects.all()}
    return render(request, "authors.html", context)


def create_author(request):
    if request.method == "POST":
        Author.objects.create(
            first_name=request.POST["first_name"],
            last_name=request.POST["last_name"],
            notes=request.POST["notes"],
        )
    return redirect("/authors")


def view_author(request, author_id):
    current_author = Author.objects.get(id=author_id)
    context = {
        "author": current_author,
        "available_books": Book.objects.exclude(authors=current_author),
    }
    return render(request, "view_author.html", context)


def add_book_to_author(request, author_id):
    if request.method == "POST":
        author_instance = Author.objects.get(id=author_id)
        book_instance = Book.objects.get(id=request.POST["book_id"])
        author_instance.books.add(book_instance)
    return redirect(f"/authors/{author_id}")
def delete_authors(request, author_id):
        author_to_delete = Author.objects.get(id=author_id)
        author_to_delete.delete()
        return redirect("/authors")