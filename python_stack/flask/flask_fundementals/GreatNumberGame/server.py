
from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = 'super_secret_game_key'

# Simple global list to act as a leaderboard for this session
leaderboard_data = []

@app.route('/')
def index():
    # 1. Initialize the game if it's the first visit
    if 'target' not in session:
        session['target'] = random.randint(1, 100)
        session['attempts'] = 0
        session['status'] = None # Too High, Too Low, Correct, or You Lose
    
    return render_template("index.html")

@app.route('/guess', methods=['POST'])
def process_guess():
    session['attempts'] += 1
    guess = int(request.form['guess'])
    target = session['target']

    # 2. Logic to determine status
    if guess < target:
        session['status'] = "too low"
    elif guess > target:
        session['status'] = "too high"
    else:
        session['status'] = "correct"

    # Sensei Bonus: Limit to 5 guesses
    if session['attempts'] >= 5 and session['status'] != "correct":
        session['status'] = "lose"

    return redirect('/')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

@app.route('/submit_score', methods=['POST'])
def submit_score():
    # Sensei Bonus: Leaderboard submission
    new_entry = {
        "name": request.form['name'],
        "attempts": session['attempts']
    }
    leaderboard_data.append(new_entry)
    # Sort leaderboard by fewest attempts
    leaderboard_data.sort(key=lambda x: x['attempts'])
    return redirect('/leaderboard')

@app.route('/leaderboard')
def leaderboard():
    return render_template("leaderboard.html", entries=leaderboard_data)

if __name__ == "__main__":
    app.run(debug=True)

