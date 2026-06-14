from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User, Message, Comment
from datetime import datetime, timedelta, timezone

def wall(request):
    if 'user_id' not in request.session:
        return redirect('/')
    
    context = {
        "user": User.objects.get(id=request.session['user_id']),
        # Newest messages first
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
    
    # Check if the message belongs to the user (Ninja Bonus)
    if message_to_delete.user.id == request.session['user_id']:
        # Check if it was made in the last 30 mins (Sensei Bonus)
        now = datetime.now(timezone.utc)
        time_diff = now - message_to_delete.created_at
        
        if time_diff.total_seconds() < 1800: # 1800 seconds = 30 minutes
            message_to_delete.delete()
        else:
            messages.error(request, "You can only delete messages within 30 minutes of posting.")
            
    return redirect('/wall')