import os
from flask import Flask
from jinja2 import Environment, PackageLoader

env = Environment(loader=PackageLoader('app', 'templates'))
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello from Mapsy!'