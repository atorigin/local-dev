from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/print')
def print():
    return 'Hello, World!2'