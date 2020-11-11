# Import dependencies
import sqlite3
from sqlite3 import Error

# Connecting to sqlite
conn = sqlite3.connect('wwii.db')
#C reating a cursor object using the cursor() method
cursor = conn.cursor()
cursor.execute("DROP TABLE IF EXISTS weather;")
# Dropping weather table if already exists.
cursor.execute("DROP TABLE IF EXISTS weather_data;")
# Creating table as per requirement
# Create weather table
cursor.execute('''CREATE TABLE weather_data(
    ID INT PRIMARY KEY,
	Date DATE ,
	MAX INT, 
	MIN INT,
	MaxTemp INT, 
	MinTemp INT,
	Precip INT, 
	WindGustSpd INT, 
	Snowfall INT, 
	PoorWeather INT, 
	PRCP INT
);''')

#-- Create a table that gives us event locations using latitudes and longitudes
# Dropping aircraft_failures table if already exists
cursor.execute("DROP TABLE IF EXISTS thor_failures;")
# Create aircraft failures table
cursor.execute('''CREATE TABLE thor_failures(
    ID INT PRIMARY KEY,
	MISSIONDATE DATE,
	LATITUDE INT, 
	LONGITUDE INT,
	WEATHERFAILS INT ,
	MECHANICALFAILS INT,
	MISCFAILS INT
);''')
# # Droping bombings table if already exists
# cursor.execute("DROP TABLE IF EXISTS bombings;")
# # Create bombings table
# cursor.execute('''CREATE TABLE bombings (
#     [id] INT IDENTITY(1,1) NOT NULL PRIMARY KEY,
#     [date] dateTime  NOT NULL ,
#     [theater] VARCHAR(25)  NOT NULL ,
#     [naf] VARCHAR(10)  NOT NULL ,
#     [country_flying_mission] VARCHAR  NOT NULL ,
#     [tgt_country] VARCHAR  NOT NULL ,
#     [tgt_city] VARCHAR  NOT NULL ,
#     [latitude] INT  NOT NULL ,
#     [longitude] INT  NOT NULL 
# );''')
# # Droping weather_stations table if already exists
# cursor.execute("DROP TABLE IF EXISTS weather_stations;")
# # Create weather_stations table
# cursor.execute('''CREATE TABLE weather_stations(
#     id serial PRIMARY KEY,
#     WBAN varchar(10),
#     NAME varchar (30),
#     State_Country varchar (30),
#     Latitude varchar (30),
#     Longitude varchar (30)
# );''')

# #DELETE FROM weather_stations
# #WHERE name = 'NAME';

# #select *
# #from weather_stations;
# # Droping weather_stations table if already exists
# cursor.execute("DROP TABLE IF EXISTS THOR_SCRAPE;")
# # Create weapons table
# cursor.execute('''CREATE TABLE THOR_SCRAPE (
#     ID serial PRIMARY KEY,
#     MSNDATE varchar,
#     THEATER varchar,
#     TGT_COUNTRY varchar,
#     TGT_LOCATION varchar,
#     LATITUDE varchar,
#     LONGITUDE varchar,
#     AircraftName varchar,
#     NumberofHighExplosives varchar,
#     TypeofHighExplosive varchar,
#     WeightofHighExplosivelbs varchar,
#     WeightofHighExplosivetons varchar,
#     NumberofIncendiaryvarchar varchar,
#     TypeofIncendiary varchar,
#     WeightofIncendiarylbs varchar,
#     WeightofIncendiarytons varchar,
#     NumberofFragmentationWeapon varchar,
#     TypeofFragmentationWeapon varchar,
#     WeightofFragmentaionWeaponlbs varchar,
#     WeightofFragmentationWeapontons varchar,
#     TotalWeightlbs varchar,
#     TotalWeighttons varchar
# );''')

#DELETE FROM THOR_SCRAPE
#WHERE MSNDATE = 'MSNDATE';

#select *
#from THOR_SCRAPE;

print("Table created successfully........")
# Commit your changes in the database
conn.commit()
#Closing the connection
conn.close()

# Dropping clean_weather and weather tables created on accident
# DROP TABLE bombings;
# DROP TABLE thor_failures;
# DROP TABLE weapons_bombs;
# DROP TABLE weather_final;
# DROP TABLE weather_stations;
# cursor.execute("""
#     DROP TABLE weather_final;
#     """)
# print("Table dropped... ")

# Commit your changes in the database
# conn.commit()

# Closing the connection
# conn.close()