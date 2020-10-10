CREATE TABLE aircraft_failure(
	missiondate DATE,
	latitude INT,
	longitude INT,
	weatherfails INT, 
	mechanicalfails INT, 
	miscfails INT
	);
    -- Create some tables so that we can load information into them - this is the "Load" part of ETL
-- Create a table that creates an Event ID using dates given
CREATE TABLE event_id(
	id INT PRIMARY KEY,
	Date DATE
);

-- Create a table that gives us event locations using latitudes and longitudes
CREATE TABLE event_location(
	event_id INT,
	MSNDATE DATE,
	LATITUDE INT, 
	LONGITUDE INT,
PRIMARY KEY(MSNDATE),
FOREIGN KEY(event_id)
	REFERENCES event_id(id)
);

-- Create a table that organizes the weapons data which we will use to create a bomb id
CREATE TABLE weapons_data(
	bomb_id INT PRIMARY KEY,
	WEAPON_NAME VARCHAR,
	WEAPON_TYPE VARCHAR
);
-- Create a table that gathers all useful weather data and organizes it by event id
CREATE TABLE weather_data(
--  event_id INT,
	date DATE,
	maxtempc FLOAT(8), 
	mintempc FLOAT(8),
	maxtempf INT, 
	mintempf INT,
	precipitation VARCHAR, 
	windgustspd FLOAT(8), 
	snowfall FLOAT(8)
--PRIMARY KEY(Date)
--FOREIGN KEY(event_id)
--	REFERENCES event_id(id)
);