import random
from datetime import datetime
from django.shortcuts import render, redirect

def index(request):
    # Initialize session if it doesn't exist
    if 'gold' not in request.session:
        request.session['gold'] = 0
        request.session['activities'] = []
    return render(request, "index.html")

def process_money(request):
    if request.method == "POST":
        location = request.POST['building']
        # Ninja Bonus: If you chose to pass via URL, you'd get this from parameters
        
        # Gold range logic based on wireframe
        if location == 'farm':
            change = random.randint(10, 20)
        elif location == 'cave':
            change = random.randint(10, 20)
        elif location == 'house':
            change = random.randint(10, 20)
        elif location == 'quest':
            change = random.randint(-50, 50)
        else:
            change = 0

        # Update total gold
        request.session['gold'] += change
        
        # Create Log entry
        timestamp = datetime.now().strftime("%Y/%m/%d %I:%M %p")
        if change >= 0:
            msg = f"Earned {change} gold from the {location}! ({timestamp})"
            color = "green"
        else:
            msg = f"Entered a quest and lost {abs(change)} gold... Ouch. ({timestamp})"
            color = "red"
        
        # Add to activities (insert at index 0 to show newest at top)
        new_activity = {'message': msg, 'class': color}
        activities = request.session['activities']
        activities.insert(0, new_activity)
        request.session['activities'] = activities # Re-save to session

    return redirect('/')

def reset(request):
    request.session.flush()
    return redirect('/')