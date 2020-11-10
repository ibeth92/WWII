-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.


SET XACT_ABORT ON

BEGIN TRANSACTION QUICKDBD

CREATE TABLE [bombings] (
    [id] INT IDENTITY(1,1) NOT NULL ,
    [date] dateTime  NOT NULL ,
    [theater] VARCHAR(25)  NOT NULL ,
    [naf] VARCHAR(10)  NOT NULL ,
    [country_flying_mission] VARCHAR  NOT NULL ,
    [tgt_country] VARCHAR  NOT NULL ,
    [tgt_city] VARCHAR  NOT NULL ,
    [latitude] INT  NOT NULL ,
    [longitude] INT  NOT NULL ,
    CONSTRAINT [PK_bombings] PRIMARY KEY CLUSTERED (
        [id] ASC
    )
)

COMMIT TRANSACTION QUICKDBD