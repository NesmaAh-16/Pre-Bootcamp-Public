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
    # We want the counter to go up by 2 total, Since redirecting to '/' increments it by 1, we add the other 1 here.
    request.session['count'] += 1
    return redirect('/')

def increment_custom(request):
    if request.method == "POST":
        amount = int(request.POST['amount'])
        #we add (amount - 1) because root route adds the final 1.
        request.session['count'] += (amount - 1)
    return redirect('/')
