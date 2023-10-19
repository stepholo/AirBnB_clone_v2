#!/usr/bin/python3
"""Module to define hello function"""

from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Function that starts a Flask web application"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Function hbnb"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """Function C_text"""
    formated_text = ' '.join(escape(text).split('_'))
    return f"C {formated_text}"


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text='is cool'):
    """Function Python_text"""
    formated_text = ' '.join(escape(text).split('_'))
    return f'Python {formated_text}'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
