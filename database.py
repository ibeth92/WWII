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

columns = inspector.get_columns('bombings')
print (columns)