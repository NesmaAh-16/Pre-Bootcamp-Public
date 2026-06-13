from django.shortcuts import render, redirect
from .models import Course, Description, Comment
from django.contrib import messages

def index(request):
    context = {
        "all_courses" : Course.objects.all()
    }
    return render(request, 'index.html', context)

def create_course(request):
    errors = Course.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    
    if request.method == 'POST':
        new_desc = Description.objects.create(content=request.POST['description'])
        Course.objects.create(
            name=request.POST['name'],
            description=new_desc     
    )
    return redirect('/')

def remove(request , id):
    context = {
        "course": Course.objects.get(id=id)
    }
    return render(request, 'remove.html',context)

def destroy(request , id):
    course_to_delete= Course.objects.get(id=id)
    course_to_delete.delete()
    return redirect('/')

def comments(request, id):
    course=Course.objects.get(id=id)
    context = {
        "course": course
        }
    return render(request, "comments.html", context)


def create_comments(request, id): 
    errors = Comment.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f'/comments/{id}')
    
    if request.method == "POST":
        course_to_comment = Course.objects.get(id=id)
        Comment.objects.create(
            content=request.POST['content'],
            course=course_to_comment
            ) 
    return redirect(f'/comments/{id}')