#!/usr/bin/python3
"""Module to define cities by states"""

from flask import Flask, render_template
from models import storage

app = Flask(__name__)

@app.teardown_appcontext
def teardown(exception):
    """removes the current SQLAchemy Session"""
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """Load all cities of a state"""
    states = sorted(list(storage.all("State").values()), key=lambda x: x.name)
    return render_template('8-cities_by_states.html', states=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
