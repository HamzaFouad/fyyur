from flask import Flask
from flask_migrate import Migrate
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

#----------------------------------------------------------------------------#
# App Config.
#----------------------------------------------------------------------------#

app = Flask(__name__)
moment = Moment(app)
app.config.from_object('config') # COMPLETE: connect to a local postgresql database
db = SQLAlchemy(app)
migrate = Migrate(app, db, compare_type=True)

#----------------------------------------------------------------------------#
# Models.
#----------------------------------------------------------------------------#

class Venue(db.Model):
    __tablename__ = 'venues'

    # from show_venue
    # id, name, genres, address, city, state, phone, website, facebook_link, seeking_talent, seeking_desription, image_link, 
    # shows {past_shows, upcoming_shows, past_shows_count, upcoming_shows_count}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    address = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    genres = db.Column(db.ARRAY(db.String(32)))
    website = db.Column(db.String(120))
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))
    seeking_talent = db.Column(db.Boolean, default=True)
    seeking_description = db.Column(db.String(500))
    
    shows_id = db.relationship('Show', backref='venues', lazy=True)

    def __repr__(self):
        return f'<Venue ID:{self.id}, Name:{self.name}>'
    
    # COMPLETE: implement any missing fields, as a database migration using Flask-Migrate

class Artist(db.Model):
    __tablename__ = 'artists'

    # from show_artist
    # id, name, genres, city, state, phone, website, facebook_link, seeking_venue, seeking_description,
    # shows {past_shows, upcoming_shows, past_shows_count, upcoming_shows_count}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    genres = db.Column(db.ARRAY(db.String(32)))
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    website = db.Column(db.String(120))
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))
    seeking_venue = db.Column(db.Boolean, default=True)
    seeking_description = db.Column(db.String(500))

    shows_id = db.relationship('Show', backref='artists', lazy=True)

    def __repr__(self):
      return f'<Artist ID:{self.id}, Name:{self.name}>'
    
    # COMPLETE: implement any missing fields, as a database migration using Flask-Migrate

# COMPLETE Implement Show and Artist models, and complete all model relationships and properties, as a database migration.

class Show(db.Model):
  __tablename__ = 'shows'

  # start_time
  # shows {past_shows, upcoming_shows, past_shows_count, upcoming_shows_count}

  id = db.Column(db.Integer, primary_key=True)
  venue_id = db.Column(db.Integer, db.ForeignKey('venues.id'), nullable=False)
  artist_id = db.Column(db.Integer, db.ForeignKey('artists.id'), nullable=False)
  start_time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

  def __repr__(self):
    return f'<Show ID:{self.id}, Venue ID:{self.venue_id}, Artist ID:{self.artist_id}>'

