#!/usr/bin/python3
"""Module to define cities by states"""

from flask import Flask, render_template
from models import storage
from models.state import State
from os import getenv

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def teardown(exception):
    """removes the current SQLAchemy Session"""
    storage.close()


@app.route('/states', strict_slashes=False)
def states_list():
    """Display a list of all states"""
    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda x: x.name)
    return render_template('9-states.html', states=sorted_states)


@app.route('/states/<id>', strict_slashes=False)
def states_cities(id):
    """Display cities of a specific state"""
    states = storage.all(State)
    state = states.get(f'State.{id}')
    if state:
        if getenv("HBNB_TYPE_STORAGE") == "db":
            cities = sorted(state.cities, key=lambda x: x.name)
        else:
            cities = state.cities()
        return render_template('9-states.html', state=state, cities=cities)
    else:
        return render_template('9-states.html', state=None)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
