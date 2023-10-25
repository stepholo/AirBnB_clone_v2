#!/usr/bin/python3
"""Starts a Flask web application"""

from flask import Flask, render_template
from models import storage

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/hbnb')
def hbnb():
    states = sorted(list(storage.all("State").values()),
                    key=lambda x: x.name)
    amenities = sorted(list(storage.all("Amenity").values()),
                       key=lambda x: x.name)
    places = sorted(list(storage.all("Place").values()),
                    key=lambda x: x.name)
    return render_template('100-hbnb.html',
                           states=states,
                           amenities=amenities,
                           places=places
                           )


@app.teardown_appcontext
def teardown_db(exception):
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
