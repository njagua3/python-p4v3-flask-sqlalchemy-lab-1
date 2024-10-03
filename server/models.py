from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin

# Create a MetaData instance for the database schema
metadata = MetaData()

# Initialize SQLAlchemy with the specified metadata
db = SQLAlchemy(metadata=metadata)

class Earthquake(db.Model, SerializerMixin):
    # Define the name of the table in the database
    __tablename__ = 'earthquakes'
    
    # Define the columns for the Earthquake model
    id = db.Column(db.Integer, primary_key=True)  # Primary key for each earthquake record
    magnitude = db.Column(db.Float, nullable=False)  # Magnitude of the earthquake (float)
    location = db.Column(db.String, nullable=False)   # Location of the earthquake (string)
    year = db.Column(db.Integer, nullable=False)      # Year when the earthquake occurred (integer)

    def __repr__(self):
        # Return a string representation of the Earthquake instance
        return f'<Earthquake {self.id}, {self.magnitude}, {self.location}, {self.year}>'
