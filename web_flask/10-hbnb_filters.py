#!/usr/bin/python3
"""Script to start a Flask web application."""
from flask import Flask, render_template
from models import storage

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def close_storage(error):
    """Remove the current SQLAlachemy Session"""
    storage.close()


@app.route('/hbnb_filters')
def hbnb_filters():
    """Display HBNB filters page."""
    stat = sorted(storage.all("State").values(), key=lambda x: x.name)
    ame = sorted(storage.all("Amenity").values(), key=lambda x: x.name)
    return render_template('10-hbnb_filters.html', stat=stat, ame=ame)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
