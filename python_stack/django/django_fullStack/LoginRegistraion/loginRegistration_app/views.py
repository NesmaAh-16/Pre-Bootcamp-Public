
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse
from .models import User
import bcrypt 

def index(request):
    return render(request, "index.html")

def register(request):
    if request.method == "POST":
        errors = User.objects.register_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        
        # Hash password and create user
        pw_hash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
        new_user = User.objects.create(
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            email=request.POST['email'],
            password=pw_hash,
            birthday=request.POST['birthday']
        )
        request.session['user_id'] = new_user.id
        return redirect('/success')
    return redirect('/')

def login(request):
    if request.method == "POST":
        user = User.objects.filter(email=request.POST['email'])
        if user:
            logged_user = user[0]
            if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
                request.session['user_id'] = logged_user.id
                return redirect('/success')
        
        messages.error(request, "Invalid email or password.")
    return redirect('/')

def success(request):
    if 'user_id' not in request.session:
        return redirect('/')
    context = { "user": User.objects.get(id=request.session['user_id']) }
    return render(request, "success.html", context)

def logout(request):
    request.session.flush()
    return redirect('/')

# AJAX Bonus: Check if email is unique as user types
def check_email(request):
    exists = User.objects.filter(email=request.GET.get('email')).exists()
    return JsonResponse({'exists': exists})