import os
from flask import Flask
from jinja2 import Environment, PackageLoader

env = Environment(loader=PackageLoader('app', 'templates'))
template = env.get_template('test_template.html')

app = Flask(__name__)



@app.route('/')
def hello():
    return 'Hello from Mapsy!'