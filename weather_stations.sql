CREATE TABLE weather_stations
(
    id serial,
    WBAN varchar(10),
    NAME varchar (30),
    State_Country varchar (30),
    Latitude varchar (30),
    Longitude varchar (30)
);

DELETE FROM weather_stations
WHERE name = 'NAME';

select *
from weather_stations;