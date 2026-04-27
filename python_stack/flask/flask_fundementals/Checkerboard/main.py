from flask import Flask,render_template
app=Flask(__name__)
@app.route('/')
def displayGrid():
    return render_template("index.html",x=8,y=8)
@app.route('/<int:x>')
def display_by_four(x):
    return render_template("index.html",x=8,y=x)
@app.route('/<int:x>/<int:y>')
def displayXbyY(x,y):
    return render_template("index.html",x=x,y=y)

@app.errorhandler(404)
def not_found(e):
    return "Sorry! No response. Try again.", 404

if __name__=="__main__":
    app.run(debug=True)

