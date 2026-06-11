from django.shortcuts import render, redirect
from .models import Show

def first(request):
    return redirect('/shows')

def index(request):
    context = {
        "all_shows": Show.objects.all()
    }
    return render(request, "index.html", context)

def new(request):
    return render(request, "new.html")

def create(request):
    if request.method =='POST':
        new_show = Show.objects.create(
        title=request.POST['title'],
        network=request.POST['network'],
        release_date=request.POST['release_date'],
        description=request.POST['description']
    )
    return redirect(f"/shows/{new_show.id}")

def show_info(request, id):
    context = {
        "show": Show.objects.get(id=id)
    }
    return render(request, "show.html", context)

def edit(request, id):
    context = {
        "show": Show.objects.get(id=id)
    }
    return render(request, "edit.html", context)

def update(request, id):
    if request.method =='POST':
        show_to_update = Show.objects.get(id=id)
        show_to_update.title = request.POST['title']
        show_to_update.network = request.POST['network']
        show_to_update.release_date = request.POST['release_date']
        show_to_update.description = request.POST['description']
        show_to_update.save()
    return redirect(f"/shows/{id}") 

def destroy(request, id):
    show_to_delete = Show.objects.get(id=id)
    show_to_delete.delete()
    return redirect("/shows")