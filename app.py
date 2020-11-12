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

# inspector = inspect(engine)
# tables = inspector.get_table_names()
# print (inspector.get_table_names())

# columns = inspector.get_columns('thor_failures')
# print (columns)

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
        f"/api/v1.0/weather_data<br/>"
        f"/api/v1.0/thor_failures<br/>"
        f"/api/v1.0/bombings<br/>"
        f"/api/v1.0/stations<br/>"
        # f"/api/v1.0/<start>/<end><br/>"
    )

# Set up Weather
@app.route("/api/v1.0/weather_data")
def weather_data():

# Create our session (link) from Python to the D
    session = Session(engine)  

# Query Weather date and conditions
    weather_rows =  session.query(str(Weather.Date), Weather.MAX, Weather.MIN, Weather.MaxTemp, Weather.MinTemp, Weather.Precip, Weather.WindGustSpd, Weather.Snowfall, Weather.PoorWeather, Weather.PRCP).all()

# Convert to list of dictionaries to jsonify
    weather_data = []
    for row in weather_rows:
        wd = collections.OrderedDict()
        wd['Date'] = row[0]
        wd['MAX'] = row[1]
        wd['MIN'] = row[2]
        wd['MaxTemp'] = row[3]
        wd['MinTemp'] = row[4]
        wd['Precip'] = row[5]
        wd['WindGustSpd'] = row[6]
        wd['Snowfall'] = row[7]
        wd['PoorWeather'] = row[8]
        wd['PRCP'] = row[9]
        weather_data.append(wd)

    weather_j = json.dumps(weather_data)

    session.close()
    
    return weather_j
    
# Set up Failures
@app.route("/api/v1.0/thor_failures")
def thor_failures():
# Create our session (link) from Python to the DB
    session = Session(engine)

# Query Weather date and conditions
    failures_rows = session.query(str(Failures.MISSIONDATE),Failures.LATITUDE, Failures.LONGITUDE, Failures.WEATHERFAILS, Failures.MECHANICALFAILS, Failures.MISCFAILS).all()

# Convert to list of dictionaries to jsonify
    failures_data = []
    for row in failures_rows:
        f = collections.OrderedDict()
        f['MISSIONDATE'] = row[0]
        f['LATITUDE'] = row[1]
        f['LONGITUDE'] = row[2]
        f['WEATHERFAILS'] = row[3]
        f['MECHANICALFAILS'] = row[4]
        f['MISCFAILS'] = row[5]
        failures_data.append(f)

    failures_j = json.dumps(failures_data)

    session.close()
    
    return failures_j

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
        b = collections.OrderedDict()
        b['date'] = row[0]
        b['theater'] = row[1]
        b['naf'] = row[2]
        b['country_flying_mission'] = row[3]
        b['tgt_country'] = row[4]
        b['tgt_city'] = row[5]
        b['lat'] = row[6]
        b['lon'] = row[7]
        bombing_data.append(b)

    j = json.dumps(bombing_data)

    session.close()
    
    return j


# Set up Weapons
@app.route("/api/v1.0/weapons")
def weapons():
# Create our session (link) from Python to the DB
    session = Session(engine)

# Query Weapons date and type
    weapon_rows = session.query(Weapons.MSNDATE, Weapons.LATITUDE, Weapons.LONGITUDE, Weapons.AircraftName, Weapons.TotalWeightlbs, Weapons.TotalWeighttons).all()

# Convert to list of dictionaries to jsonify
    weapons_data = []

    for row in weapon_rows:
        w = collections.OrderedDict()
        w['MSNDATE'] = row[0]
        w['LATITUDE'] = row[1]
        w['LONGITUDE'] = row[2]
        w['AircraftName'] = row[3]
        w['TotalWeightlbs'] = row[4]
        w['TotalWeighttons'] = row[5]
        weapons_data.append(w)

    weapon_j = json.dumps(weapons_data)

    session.close()

    return jsonify(weapon_j)


# Set up Stations
@app.route("/api/v1.0/stations")
def stations():

# Create our session (link) from Python to the DB
    session = Session(engine)

    stations = []

# Query all stations
    station_rows = session.query(Station.WBAN, Station.NAME, Station.State_Country, Station.Latitude, Station.Longitude).all()
    for row in station_rows:
        s = collections.OrderedDict()
        s['WBAN'] = row[0]
        s['NAME'] = row[1]
        s['State_Country'] = row[2]
        s['Latitude'] = row[3]
        s['Longitude'] = row[4]
        stations.append(s)

    station_j = json.dumps(stations)
    session.close()
 
    return jsonify(station_j)

if __name__ == "__main__":
    app.run(debug=True)