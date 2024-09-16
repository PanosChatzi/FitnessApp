USE [myFitnessApp]

CREATE TABLE FitnessData (
    AthleteId VARCHAR(50) NOT NULL,
    ActivityId BIGINT NOT NULL,
    Type VARCHAR(50) NOT NULL,
    Date DATETIME NOT NULL,
    Distance FLOAT NOT NULL,
    MovingTime FLOAT NOT NULL,
    Name VARCHAR(255) NOT NULL,
    AvgHR INT NULL,
    IntensityPercent INT NOT NULL,
    AvgAltitude FLOAT NOT NULL,
    AvgHRPercent INT NULL,
    ElapsedTime FLOAT NOT NULL,
    HRRc INT NULL,
    kcal INT NOT NULL,
    MaxAltitude FLOAT NOT NULL,
    MaxHR INT NULL,
    MaxHRPercent INT NULL,
    Pace VARCHAR(10) NOT NULL,
    PRIMARY KEY (AthleteId, ActivityId)  -- Composite Primary Key
);

