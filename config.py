import os
SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# Connect to the database

# COMPLETE IMPLEMENT DATABASE URL
SQLALCHEMY_DATABASE_URI = 'postgres://postgres:pw@localhost:5432/fyyurdb' # using the default user with no password

# Suppress console warnings
SQLALCHEMY_TRACK_MODIFICATIONS = False