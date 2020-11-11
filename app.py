# Import dependencies
import numpy as np
import pandas as pd
import os
import json
import collections
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, inspect

import flask 
from flask import Flask, jsonify

# Setup Flask
# Create an app, pass to __name__
app = Flask(__name__)

# Setup Database
engine = create_engine('sqlite:///wwii.db')

# Automap base
Base = automap_base()

# Reflect an existing database into a new model
Base.prepare(engine, reflect= True)

inspector = inspect(engine)
tables = inspector.get_table_names()
# print (inspector.get_table_names())

#columns = inspector.get_columns('bombings')
#print (columns)

# Create for loop that prints table names and columns
# for table in tables:
#     columns = inspector.get_columns(table)
#     print (columns)
#     print (table)
# print(Base.classes)
# Save references to each table
Weapons = Base.classes.THOR_SCRAPE
Weather = Base.classes.weather_data
Failures = Base.classes.thor_failures
Bombings = Base.classes.bombings
Station = Base.classes.weather_stations
session = Session(engine)

@app.route("/")
def welcome():
    return(
        f"A Day in History WWII<br/>"
        f"Avaialble Routes:<br/>"
        f"/api/v1.0/weapons<br/>"
        f"/api/v1.0/weather<br/>"
        f"/api/v1.0/failures<br/>"
        f"/api/v1.0/bombings<br/>"
        f"/api/v1.0/stations<br/>"
 #       f"/api/v1.0/<start>/<end><br/>"
    )

# Set up Weather
@app.route("/api/v1.0/weather")
def weather():
# Create our session (link) from Python to the D
    session = Session(engine)   
# Query Weather date and conditions
    results =   session.query(Weather.Date, Weather.MAX, Weather.MIN, Weather.MaxTemp, Weather.MinTemp, Weather.Precip, Weather.WindGustSpd, Weather.Snowfall, Weather.PoorWeather, Weather.PRCP).\
                order_by(Weather.Date).all()
    for result in results:
        return print(result)

# # Convert to list of dictionaries to jsonify
#     weather_data = []

#     for result in results:
#         weather_data.append(result)

#     session.close()
#     # # Convert list of tuples into normal list
#     # all_weather = list(np.ravel(results)
#     return jsonify(weather_data)

# Set up Failures
@app.route("/api/v1.0/thor_failures")
def thor_failures():
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
    rows = session.query(str(Bombings.date),Bombings.theater, Bombings.naf, Bombings.country_flying_mission, Bombings.tgt_country, Bombings.tgt_city, Bombings.latitude, Bombings.longitude).all()

# Convert to list of dictionaries to jsonify
    bombing_data = []
    for row in rows:
        d = collections.OrderedDict()
        d['date'] = row[0]
        d['theater'] = row[1]
        d['naf'] = row[2]
        d['country_flying_mission'] = row[3]
        d['tgt_country'] = row[4]
        d['tgt_city'] = row[5]
        d['lat'] = row[6]
        d['lon'] = row[7]
        bombing_data.append(d)

    j = json.dumps(bombing_data)

    session.close()
    
    return j

if __name__ == "__main__":
    app.run(debug=True)

# Set up Weapons
# @app.route("/api/v1.0/weapons")
# def weapons():
# Create our session (link) from Python to the DB
#     session = Session(engine)

# Query Weapons date and type
#     results =   session.query(Weapons.date, Weapons.type).\
#                 order_by(Weapons.date).all()

# Convert to list of dictionaries to jsonify
#     weapons_data = []

#     for date, type in results:
#         new_dict = {}
#         new_dict[date] = type
#         weapons_data.append(new_dict)

#     session.close()

#     return jsonify(weapons_data)


# Set up Stations
# @app.route("/api/v1.0/stations")
# def stations():

# Create our session (link) from Python to the DB
#     session = Session(engine)

#     stations = {}

# Query all stations
#     results = session.query(Station.station, Station.name).all()
#     for sta, name in results:
#         stations[sta] = name

#     session.close()
 
#     return jsonify(stations)

