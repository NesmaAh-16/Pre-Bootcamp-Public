from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    # Renders the initial form page
    return render_template("index.html")

@app.route('/result', methods=['POST'])
def result():
    # Extracting data from the POST request
    # 'name' inside request.form corresponds to the 'name' attribute in HTML inputs
    user_data = {
        "name": request.form['name'],
        "location": request.form['location'],
        "language": request.form['language'],
        "comments": request.form['comments'],
        "experience": request.form.get('experience'), # Radio button (Ninja Bonus)
        "interests": request.form.getlist('interests') # Checkboxes (Sensei Bonus)
    }
    
    print(request.form) # Useful for debugging in terminal
    return render_template("result.html", data=user_data)

if __name__ == "__main__":
    app.run(debug=True, port=5000)

