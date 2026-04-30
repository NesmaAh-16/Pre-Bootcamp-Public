from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe' # Required for session to work

@app.route('/')
def index():
    # Sensei Bonus: Track actual page visits separately
    if 'visits' not in session:
        session['visits'] = 1
    else:
        session['visits'] += 1

    # Track counter value (initialized to 0 if new session)
    if 'count' not in session:
        session['count'] = 0
    
    # Increment the counter for the current visit
    session['count'] += 1
        
    return render_template("index.html")

@app.route('/destroy_session')
def destroy():
    session.clear() # Removes everything from session
    return redirect('/')

@app.route('/add_two')
def add_two():
    # Logic: we add 1 here, because the redirect back to '/' 
    # will automatically add the second 1, resulting in +2.
    session['count'] += 1
    return redirect('/')

@app.route('/reset')
def reset():
    # Resets only the counter, not the total visit history
    session['count'] = 0 
    return redirect('/')

@app.route('/increment', methods=['POST'])
def increment():
    # Sensei Bonus: Custom increment from a form
    # We subtract 1 because the redirect back to '/' adds 1 automatically
    amount = int(request.form['amount'])
    session['count'] += (amount - 1)
    return redirect('/') #ٌReload the page ==> visit+=1

if __name__ == "__main__":
    app.run(debug=True)
