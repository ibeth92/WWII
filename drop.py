# Import dependencies
import sqlite3
from sqlite3 import Error


# Connecting to sqlite
conn = sqlite3.connect('wwii.db')
#C reating a cursor object using the cursor() method
cursor = conn.cursor()
# Dropping weather table if already exists.
cursor.execute("DROP TABLE IF EXISTS weapons_bombs;")

cursor.execute("DROP TABLE IF EXISTS weather;")
# Creating table as per requirement
# Create weather table

cursor.execute("DROP TABLE IF EXISTS aircraft_failures;")
# Create aircraft failures table

# Commit your changes in the database
conn.commit()
#Closing the connection
conn.close()