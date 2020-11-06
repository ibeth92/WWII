import sqlite3
from sqlite3 import Error

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, inspect

# conn = sqlite3.connect('wwii.db')

# Import Flask 
# from flask import Flask, jsonify

# Setup Database
engine = create_engine('sqlite:///wwii.db')

# Automap base
Base = automap_base()

inspector = inspect(engine)
print (inspector.get_table_names())

#columns = inspector.get_columns('bombings')
#print (columns)

# Connect to sqlite
conn = sqlite3.connect('wwii.db')

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

# Dropping clean_weather and weather tables created on accident
# cursor.execute("""
# DROP TABLE weather;
# DROP TABLE clean_weather;
# """")
# print("Table dropped... ")

#Commit your changes in the database
conn.commit()

#Closing the connection
conn.close()