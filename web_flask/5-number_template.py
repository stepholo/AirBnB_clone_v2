#!/usr/bin/python3
"""Module to define hello function"""

from flask import Flask, render_template
from markupsafe import escape

app = Flask(__name__, template_folder='templates')


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


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """Function number"""
    return f'{escape(n)} is a number'


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n=None):
    """Function number_template"""
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
