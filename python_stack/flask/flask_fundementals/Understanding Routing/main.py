from flask import Flask 

my_app = Flask(__name__)
@my_app.route('/')
def hiFlask():
    return 'Hi World!'
@my_app.route('/<name>')
def show_name(name):
    return name
@my_app.route('/say/<name>')
def say_name(name):
    return "Hi "+ name + "!"
@my_app.route('/repeat/<int:times>/<name>')
def repeat(times,name):
    return  (name +" ")* times
#@my_app.errorhandler(404)
#def not_found(e):
    #return "Sorry! No response. Try again."
@my_app.errorhandler(404)
def not_found(e):
    return """
    <h1>404 - Not Found</h1>
    <p>Sorry! No response. Try again.</p>
    <a href="/">Go Home</a>
    """, 404   
if __name__=="__main__":
    my_app.run(debug=True)