import random
from django.shortcuts import render, redirect

def index(request):
    # Initialize game if target doesn't exist
    if 'target' not in request.session:
        request.session['target'] = random.randint(1, 100)
        request.session['attempts'] = 0
        request.session['status'] = None # 'too_high', 'too_low', 'win', 'lose'
        request.session['winners'] = request.session.get('winners', []) # Sensei: persistent leaderboard
    return render(request, "index.html")

def guess(request):
    if request.method == "POST":
        val = int(request.POST['guess'])
        request.session['attempts'] += 1
        target = request.session['target']

        if val == target:
            request.session['status'] = 'win'
        elif val > target:
            request.session['status'] = 'too_high'
        else:
            request.session['status'] = 'too_low'

        # Sensei Bonus: Limit to 5 attempts
        if request.session['attempts'] >= 5 and request.session['status'] != 'win':
            request.session['status'] = 'lose'

    return redirect('/')

def reset(request):
    # Clear game state but preserve leaderboard
    request.session.pop('target')
    request.session.pop('attempts')
    request.session.pop('status')
    return redirect('/')

def submit_leaderboard(request):
    if request.method == "POST":
        # Add winner to the list in session
        new_winner = {
            'name': request.POST['name'],
            'count': request.session['attempts']
        }
        winners = request.session.get('winners', [])
        winners.append(new_winner)
        request.session['winners'] = winners
        return redirect('/leaderboard')
    return redirect('/')

def leaderboard(request):
    return render(request, "leaderboard.html")