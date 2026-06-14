from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User, Author, Book, Review
import bcrypt

# --- Login & Registration ---

def index(request):
    return render(request, 'index.html')

def register(request):
    errors = User.objects.register_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    
    hash_pw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
    user = User.objects.create(
        name=request.POST['name'],
        alias=request.POST['alias'],
        email=request.POST['email'],
        password=hash_pw
    )
    request.session['user_id'] = user.id
    return redirect('/books')

def login(request):
    user = User.objects.filter(email=request.POST['email'])
    if user:
        logged_user = user[0]
        if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
            request.session['user_id'] = logged_user.id
            return redirect('/books')
    
    messages.error(request, "Invalid Blog/Password")
    return redirect('/')

def logout(request):
    request.session.flush()
    return redirect('/')

# --- Books & Reviews ---

def books_home(request):
    if 'user_id' not in request.session:
        return redirect('/')
    context = {
        'user': User.objects.get(id=request.session['user_id']),
        'recent_reviews': Review.objects.order_by('-created_at')[:3],
        'other_books': Book.objects.all()
    }
    return render(request, 'books_home.html', context)

def add_book_page(request):
    if 'user_id' not in request.session:
        return redirect('/')
    context = {
        'all_authors': Author.objects.all()
    }
    return render(request, 'add_book.html', context)

def create_book(request):
    # Logic for Author (Existing vs New)
    if request.POST['new_author']:
        author = Author.objects.create(name=request.POST['new_author'])
    else:
        author = Author.objects.get(id=request.POST['author_id'])
    
    book = Book.objects.create(title=request.POST['title'], author=author)
    
    Review.objects.create(
        content=request.POST['review'],
        rating=request.POST['rating'],
        user=User.objects.get(id=request.session['user_id']),
        book=book
    )
    return redirect(f'/books/{book.id}')

def show_book(request, book_id):
    context = {
        'book': Book.objects.get(id=book_id)
    }
    return render(request, 'show_book.html', context)

def create_review(request, book_id):
    Review.objects.create(
        content=request.POST['review'],
        rating=request.POST['rating'],
        user=User.objects.get(id=request.session['user_id']),
        book=Book.objects.get(id=book_id)
    )
    return redirect(f'/books/{book_id}')

def delete_review(request, review_id):
    review = Review.objects.get(id=review_id)
    if review.user.id == request.session['user_id']:
        review.delete()
    return redirect(request.META.get('HTTP_REFERER'))

def show_user(request, user_id):
    context = {
        'user': User.objects.get(id=user_id)
    }
    return render(request, 'show_user.html', context)