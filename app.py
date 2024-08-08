from flask import Flask, request
import json
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/webhook',methods=['POST'])
def print():
    print(json.dumps(request.get_json(), indent = 4))
    return 'ok'