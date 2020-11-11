# Import dependencies
import sqlite3
from sqlite3 import Error


# Connecting to sqlite
conn = sqlite3.connect('wwii.db')
#C reating a cursor object using the cursor() method
cursor = conn.cursor()
# Dropping weather table if already exists.
cursor.execute("DROP TABLE IF EXISTS weapons_bombs;")

cursor.execute('''CREATE TABLE weapons_bombs (
    ID serial PRIMARY KEY,
    MSNDATE varchar,
    THEATER varchar,
    TGT_COUNTRY varchar,
    TGT_LOCATION varchar,
    LATITUDE varchar,
    LONGITUDE varchar,
    AircraftName varchar,
    NumberofHighExplosives varchar,
    TypeofHighExplosive varchar,
    WeightofHighExplosivelbs varchar,
    WeightofHighExplosivetons varchar,
    NumberofIncendiary varchar,
    TypeofIncendiary varchar,
    WeightofIncendiarylbs varchar,
    WeightofIncendiarytons varchar,
    NumberofFragmentationWeapon varchar,
    TypeofFragmentationWeapon varchar,
    WeightofFragmentaionWeaponlbs varchar,
    WeightofFragmentationWeapontons varchar,
    TotalWeightlbs varchar,
    TotalWeighttons varchar
);''')

# Commit your changes in the database
conn.commit()
#Closing the connection
conn.close()