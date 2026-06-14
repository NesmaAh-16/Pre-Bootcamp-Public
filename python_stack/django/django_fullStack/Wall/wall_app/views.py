from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User, Message, Comment
from datetime import datetime, timedelta, timezone
import bcrypt

# --- LOGIN & REGISTRATION ---
def index(request):
    return render(request, 'index.html')

def register(request):
    errors = User.objects.validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    
    hash_pw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
    new_user = User.objects.create(
        first_name=request.POST['first_name'],
        last_name=request.POST['last_name'],
        email=request.POST['email'],
        password=hash_pw
    )
    request.session['user_id'] = new_user.id
    request.session['first_name'] = new_user.first_name
    return redirect('/wall')

def login(request):
    user = User.objects.filter(email=request.POST['email'])
    if user:
        logged_user = user[0]
        if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
            request.session['user_id'] = logged_user.id
            request.session['first_name'] = logged_user.first_name
            return redirect('/wall')
    
    messages.error(request, "Invalid email or password")
    return redirect('/')

def logout(request):
    request.session.flush()
    return redirect('/')

# --- WALL LOGIC ---
def wall(request):
    if 'user_id' not in request.session:
        return redirect('/')
    
    context = {
        "user": User.objects.get(id=request.session['user_id']),
        "all_messages": Message.objects.all().order_by("-created_at") 
    }
    return render(request, 'wall.html', context)

def post_message(request):
    if request.method == "POST":
        Message.objects.create(
            message = request.POST['message'],
            user = User.objects.get(id=request.session['user_id'])
        )
    return redirect('/wall')

def post_comment(request, message_id):
    if request.method == "POST":
        Comment.objects.create(
            comment = request.POST['comment'],
            user = User.objects.get(id=request.session['user_id']),
            message = Message.objects.get(id=message_id)
        )
    return redirect('/wall')

def delete_message(request, message_id):
    message_to_delete = Message.objects.get(id=message_id)
    if message_to_delete.user.id == request.session['user_id']:
        now = datetime.now(timezone.utc)
        time_diff = now - message_to_delete.created_at
        if time_diff.total_seconds() < 1800:
            message_to_delete.delete()
        else:
            messages.error(request, "You can only delete messages within 30 minutes.")
    return redirect('/wall') 