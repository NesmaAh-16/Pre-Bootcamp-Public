from django.shortcuts import render, redirect

def index(request):
    return render(request, 'index.html')

def create_user(request):
    if request.method == "POST":
        context = {
            "first_name": request.POST['first_name'],
            "last_name": request.POST['last_name'],
            "age": request.POST['age'],
            "email": request.POST['email'],
            "favorite_subject": request.POST['favorite_subject']
        }
   
        return render(request, 'result.html', context)
    
    return redirect('/')

def result_user(request):
    return redirect('/')