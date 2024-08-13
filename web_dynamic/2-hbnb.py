#!/usr/bin/python3
""" Starts a Flash Web Application """

import uuid
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from os import environ
from flask import Flask, render_template

app = Flask(__name__)
app.jinja_env.trim_blocks = True  # Enable trimming of blocks in Jinja2 templates
app.jinja_env.lstrip_blocks = True  # Enable stripping leading whitespace from Jinja2 templates

@app.teardown_appcontext
def close_db(error):
    """ Remove the current SQLAlchemy Session """
    storage.close()

    @app.route('/2-hbnb/', strict_slashes=False)
    def hbnb():
        """ HBNB is alive! """
        cache_id = str(uuid.uuid4())
        states = storage.all(State).values()
        states = sorted(states, key=lambda k: k.name)
        st_ct = []

        for state in states:
            st_ct.append([state, sorted(state.cities, key=lambda k: k.name)])

        amenities = storage.all(Amenity).values()
        amenities = sorted(amenities, key=lambda k: k.name)

        places = storage.all(Place).values()
        places = sorted(places, key=lambda k: k.name)

        return render_template('0-hbnb.html',
                                states=st_ct,
                                amenities=amenities,
                                places=places,
                                cache_id=cache_id)  # Pass cache_id to the template

    if __name__ == "__main__":
        """ Main Function """ 
        app.run(host=environ.get("HBNB_HOST", "0.0.0.0"),
            port=int(environ.get("HBNB_PORT", 5000)))

