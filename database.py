import sqlite3
from sqlite3 import Error

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, inspect

# Import Flask 
# from flask import Flask, jsonify

# Setup Database
engine = create_engine('sqlite:///wwii.db')

# Automap base
Base = automap_base()

inspector = inspect(engine)
tables = inspector.get_table_names()
print (inspector.get_table_names())

#columns = inspector.get_columns('bombings')
#print (columns)

# Connect to sqlite
# conn = sqlite3.connect('wwii.db')

# Creating a cursor object using the cursor() method
# cursor = conn.cursor()

# Dropping clean_weather and weather tables created on accident
# cursor.execute("""
# DROP TABLE weather;
# DROP TABLE clean_weather;
# """")
# print("Table dropped... ")

# Commit your changes in the database
# conn.commit()

# Closing the connection
# conn.close()

# Create for loop that prints table names and columns
for table in tables:
    columns = inspector.get_columns(table)
    print (columns)
    print (table)

# Reflect an existing database into a new model
Base.prepare(engine, reflect= True)

# Save references to each table
Weapons = Base.classes.weapons
Weather = Base.classes.weather 
Failures = Base.classes.failures
Bombings = Base.classes.bombings
Stations = Base.classes.stations
session = Session(engine)

# Setup Flask
# Create an app, pass to __name__
app = Flask(__name__)

@app.route("/")
def welcome():
    return(
        f"A Day in History WWII<br/>"
        f"Avaialble Routes:<br>"
        f"/api/v1.0/weapons<br/>"
        f"/api/v1.0/weather<br/>"
        f"/api/v1.0/failures<br/>"
        f"/api/v1.0/bombings<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/<start>/<end><br/>"
    )
# Set up Weapons
@app.route("/api/v1.0/weapons")
def weapons():
# Create our session (link) from Python to the DB
    session = Session(engine)

# Query Weapons date and type
    results =   session.query(Weapons.date, Weapons.type).\
                order_by(Weapons.date).all()

# Convert to list of dictionaries to jsonify
    weapons_data = []

    for date, type in results:
        new_dict = {}
        new_dict[date] = type
        weapons_data.append(new_dict)

    session.close()

    return jsonify(weapons_data)

# Set up Weather
@app.route("/api/v1.0/weather")
def weather():
# Create our session (link) from Python to the DB
    session = Session(engine)

# Query Weather date and conditions
    results =   session.query(Weather.date, Weather.type).\
                order_by(Weather.date).all()

# Convert to list of dictionaries to jsonify
    weather_data = []

    for date, type in results:
        new_dict = {}
        new_dict[date] = type
        weather_data.append(new_dict)

    session.close()

    return jsonify(weather_data)

# Set up Failures
@app.route("/api/v1.0/failures")
def failures():
# Create our session (link) from Python to the DB
    session = Session(engine)

# Query Weather date and conditions
    results =   session.query(Failures.date, Failures.type).\
                order_by(Failures.date).all()

# Convert to list of dictionaries to jsonify
    failures_data = []

    for date, type in results:
        new_dict = {}
        new_dict[date] = type
        failures_data.append(new_dict)

    session.close()

    return jsonify(failures_data)

# Set up Bombings
@app.route("/api/v1.0/bombings")
def bombings():

# Create our session (link) from Python to the DB
    session = Session(engine)

# Query Weather date and conditions
    results =   session.query(Bombings.date, Bombings.type).\
                order_by(Bombings.date).all()

# Convert to list of dictionaries to jsonify
    bombings_data = []

    for date, type in results:
        new_dict = {}
        new_dict[date] = type
        bombings_data.append(new_dict)

    session.close()

    return jsonify(bombings_data)

# Set up Stations
@app.route("/api/v1.0/stations")
def stations():

# Create our session (link) from Python to the DB
    session = Session(engine)

    stations = {}

# Query all stations
    results = session.query(Station.station, Station.name).all()
    for sta, name in results:
        stations[sta] = name

    session.close()
 
    return jsonify(stations)


