
CREATE TABLE THOR_SCRAPE
(
    ID serial,
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
    NumberofIncendiaryvarchar varchar,
    TypeofIncendiary varchar,
    WeightofIncendiarylbs varchar,
    WeightofIncendiarytons varchar,
    NumberofFragmentationWeapon varchar,
    TypeofFragmentationWeapon varchar,
    WeightofFragmentaionWeaponlbs varchar,
    WeightofFragmentationWeapontons varchar,
    TotalWeightlbs varchar,
    TotalWeighttons varchar
);

DELETE FROM THOR_SCRAPE
WHERE MSNDATE = 'MSNDATE';

select *
from THOR_SCRAPE;