from django.shortcuts import render, redirect

def index(request):
    if 'count' not in request.session:
        request.session['count'] = 0
    if 'visits' not in request.session:
        request.session['visits'] = 0

    request.session['count'] += 1
    request.session['visits'] += 1
    
    return render(request, "index.html")

def destroy(request):
    # Clear the entire session
    request.session.flush()
    return redirect('/')

def add_two(request):
    # + 2 total, and redirecting to '/' increments it by 1, we add the other 1 here.
    request.session['count'] += 1
    return redirect('/')

def increment(request):
    if request.method == "POST":
        amount = int(request.POST['amount'])
        #add (amount - 1) because root route adds the final 1.
        request.session['count'] += (amount - 1)
    return redirect('/')
