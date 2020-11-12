# Import dependencies
import sqlite3
from sqlite3 import Error


# Connecting to sqlite
conn = sqlite3.connect('wwii.db')
#C reating a cursor object using the cursor() method
cursor = conn.cursor()
# Dropping weather table if already exists.
cursor.execute("DROP TABLE IF EXISTS THOR_SCRAPE;")

cursor.execute("DROP TABLE IF EXISTS bombings;")
# Creating table as per requirement
# Create weather table

cursor.execute("DROP TABLE IF EXISTS thor_failures;")
cursor.execute("DROP TABLE IF EXISTS weather_data;")
cursor.execute("DROP TABLE IF EXISTS weather_stations;")
cursor.execute("DROP TABLE IF EXISTS wwii_data;")
# Create aircraft failures table
print('tables dropped')
# Commit your changes in the database
conn.commit()
#Closing the connection
conn.close()