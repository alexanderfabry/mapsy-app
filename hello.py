import os
from flask import Flask
from jinja2 import Environment, PackageLoader

env = Environment(loader=PackageLoader('app', 'templates'))
template = env.get_template('test_template.html')
css = env.get_template('mapsy.css')
mapsy_js = env.get_template('mapsy.js')

app = Flask(__name__)


@app.route('/')
def hello():
    return template.render(css_styles=css.render(), mapsy_js=mapsy_js.render())