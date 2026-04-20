from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'  # You need this to see something in the browser

if __name__=="__main__":
    app.run(debug=True)