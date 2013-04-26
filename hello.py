import os
from flask import Flask
from jinja2 import Environment, PackageLoader

env = Environment(loader=PackageLoader('app', 'templates'))
template = env.get_template('test_template.html')

app = Flask(__name__)

def get_resource_as_string(name, charset='utf-8'):
    with app.open_resource(name) as f:
        return f.read().decode(charset)
        
app.jinja_env.globals['get_resource_as_string'] = get_resource_as_string

@app.route('/')
def hello():
    return template.render(the='variables', go='here')