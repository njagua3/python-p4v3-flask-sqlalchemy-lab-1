#!/usr/bin/env python3

from flask import Flask, make_response, jsonify
from flask_migrate import Migrate
from models import db, Earthquake

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)

@app.route('/')
def index():
    body = {'message': 'Flask SQLAlchemy Lab 1'}
    return make_response(body, 200)

# Add views here
@app.route('/earthquakes/<int:id>')
def get_earthquake(id):
    # Create a session and use the new method to get the earthquake by ID
    with db.session() as session:
        earthquake = session.get(Earthquake, id)
    
    if earthquake is None:
        # Return a JSON response with an error message if not found
        return jsonify({'message': f'Earthquake {id} not found.'}), 404
    
    # Return a JSON response with the earthquake attributes
    return jsonify({
        'id': earthquake.id,
        'magnitude': earthquake.magnitude,
        'location': earthquake.location,
        'year': earthquake.year
    })
@app.route('/earthquakes/magnitude/<float:magnitude>')
def get_earthquakes_by_magnitude(magnitude):
    # Create a session and use the new method to get earthquakes with magnitude >= the parameter value
    with db.session() as session:
        earthquakes = session.query(Earthquake).filter(Earthquake.magnitude >= magnitude).all()
    
    # Return a JSON response with the count of earthquakes and the list of matching earthquakes
    return jsonify({
        'count': len(earthquakes),
        'quakes': [
            {
                'id': earthquake.id,
                'magnitude': earthquake.magnitude,
                'location': earthquake.location,
                'year': earthquake.year
            } for earthquake in earthquakes
        ]
    })

if __name__ == '__main__':
    app.run(port=5555, debug=True)
