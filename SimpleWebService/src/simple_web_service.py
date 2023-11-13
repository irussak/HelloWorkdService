#!/bin/python3

from flask import Flask
from config import SERVER_HOST, SERVER_PORT

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World!'

app.run(host=SERVER_HOST, port=SERVER_PORT)
