# Import dependencies
import os
import json
import collections
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, inspect
import flask 
from flask import Flask, jsonify, render_template
from flask_cors import cross_origin 

# Setup Flask
# Create an app, pass to __name__
app = Flask(__name__)

from flask_sqlalchemy import SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('postgres://lzxwacdzlrivzn:3ac1a7944d2989535d6ed9f6f3f995ba4196f62c177d3980e068b5e35d51a60c@ec2-23-20-168-40.compute-1.amazonaws.com:5432/d1l75mfrn10irh', '')

# Remove tracking modifications
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Setup Database
engine = create_engine('sqlite:///wwii.db')

# Automap base
Base = automap_base()

# Reflect an existing database into a new model
Base.prepare(engine, reflect= True)


WWII = Base.classes.wwii_data
session = Session(engine)

@app.route("/", methods=['GET'])
@cross_origin()
def homepage():
    return render_template('index.html')

@app.route("/api/v1.0/home", methods=['GET'])
@cross_origin()
def welcome():
    return(
        f"A Day in History WWII<br/>"
        f"Avaialble Routes:<br/>"
        f"/api/v1.0/wwii_data<br/>"
        f"/api/v1.0/wwii_map<br/>"
)

# Set up Weather
@app.route("/api/v1.0/wwii_data", methods=['GET'])
@cross_origin()
def wwii_data():

# Create our session (link) from Python to the D
    session = Session(engine)  

# Query Weather date and conditions
    wwii_rows =  session.query(str(WWII.MSNDATE), WWII.THEATER, WWII.NAF, WWII.COUNTRY_FLYING_MISSION, WWII.TGT_COUNTRY, WWII.TGT_LOCATION, WWII.LATITUDE, WWII.LONGITUDE, WWII.AIRCRAFT_NAME, WWII.MAX, WWII.MAX).all()

# Convert to list of dictionaries to jsonify
    wwii = []
    for row in wwii_rows:
        wm = collections.OrderedDict()
        wm['DATE'] = row[0]
        wm['THEATER'] = row[1]
        wm['NAF'] = row[2]
        wm['COUNTRY_FLYING_MISSION'] = row[3]
        wm['TGT_COUNTRY'] = row[4]
        wm['TGT_LOCATION'] = row[5]
        wm['LATITUDE'] = row[6]
        wm['LONGITUDE'] = row[7]
        wm['AIRCRAFT_NAME'] = row[8]
        wm['MAX'] = row[9]
        wm['MIN'] = row[10]
        wwii.append(wm)

    weather_j = json.dumps(wwii)

    session.close()
    
    return jsonify(weather_j)

@app.route("/api/v1.0/wwii_map", methods=['GET'])
@cross_origin()
def wwii_map():

# Create our session (link) from Python to the D
    session = Session(engine)  

# Query Weather date and conditions
    wwii_map_rows =  session.query(str(WWII.MSNDATE), WWII.LATITUDE, WWII.LONGITUDE).all()

# Convert to list of dictionaries to jsonify
    wwii_map = []
    for row in wwii_map_rows:
        wm = collections.OrderedDict()
        wm['DATE'] = row[0]
        wm['LATITUDE'] = row[1]
        wm['LONGITUDE'] = row[2]
        wwii_map.append(wm)

    maps_j = json.dumps(wwii_map)

    session.close()
    
    return jsonify(maps_j)
    

if __name__ == "__main__":
    app.run(debug=True)