from flask import Flask,render_template
app=Flask(__name__)
@app.route('/play')
def showBoxes():
    return render_template("index.html",x=3,color="blue")
@app.route('/play/<int:x>')
def repeat_boxes(x):
    return render_template("index.html",color="blue",x=x)
@app.route('/play/<int:x>/<color>')
def repeat_boxes_color(x,color):
    return render_template("index.html",x=x,color=color)

@app.errorhandler(404)
def not_found(e):
    return "Sorry! No response. Try again.", 404
if __name__=="__main__":
    app.run(debug=True)









