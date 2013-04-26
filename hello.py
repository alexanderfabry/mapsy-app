import os
from flask import Flask, make_response, redirect
from jinja2 import Environment, PackageLoader

from functools import wraps

env = Environment(loader=PackageLoader('app', 'templates'))
template = env.get_template('test_template.html')
css = env.get_template('mapsy.css')
mapsy_js = env.get_template('mapsy.js')

app = Flask(__name__)


def add_response_headers(headers={}):
    """This decorator adds the headers passed in to the response"""
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            resp = make_response(f(*args, **kwargs))
            h = resp.headers
            for header, value in headers.items():
                h[header] = value
            return resp
        return decorated_function
    return decorator

def contenttypejson(f):
    """This decorator passes Content-Type: application/json"""
    @wraps(f)
    @add_response_headers({'Content-Type': 'application/json'})
    def decorated_function(*args, **kwargs):
        return f(*args, **kwargs)
    return decorated_function

def contenttypetextplain(f):
    """This decorator passes Content-Type: text/plain"""
    @wraps(f)
    @add_response_headers({'Content-Type': 'text/plain'})
    def decorated_function(*args, **kwargs):
        return f(*args, **kwargs)
    return decorated_function

def noindex(f):
    """This decorator passes X-Robots-Tag: noindex"""
    @wraps(f)
    @add_response_headers({'X-Robots-Tag': 'noindex'})
    def decorated_function(*args, **kwargs):
        return f(*args, **kwargs)
    return decorated_function

@app.route('/')
def hello():
    return template.render(css_styles=css.render(), mapsy_js=mapsy_js.render())

@app.route('/shows')
@contenttypetextplain
@noindex
def show_post():
    return "hello"