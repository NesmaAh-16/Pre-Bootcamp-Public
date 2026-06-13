from django.shortcuts import render, redirect
from .models import *

def index(request):
    context = {
        "all_courses" : Course.objects.all()
    }
    return render(request, 'index.html', context)

def create_course(request):
    if request.method == 'POST':
        new_course=Course.objects.create(
            name=request.POST['name'],
            description=request.POST['description']     
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