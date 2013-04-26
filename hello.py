import os
from flask import Flask
from jinja2 import Environment, PackageLoader

env = Environment(loader=PackageLoader('app', 'templates'))
template = env.get_template('test_template.html')
css = env.get_template('mapsy.css')

app = Flask(__name__)


@app.route('/')
def hello():
    return template.render(css_styles='#something-else{ border:1px solid black; }')