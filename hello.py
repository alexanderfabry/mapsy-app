import os
from flask import Flask
import jinja2

env = Environment(loader=PackageLoader('app', 'templates'))
template = env.get_template('test_template.html')

app = Flask(__name__)

def include_file(name):
    return jinja2.Markup(loader.get_source(env, name)[0])

loader = jinja2.PackageLoader(__name__, 'templates')
env = jinja2.Environment(loader=loader)
env.globals['include_file'] = include_file

@app.route('/')
def hello():
    return template.render(the='variables', go='here')






