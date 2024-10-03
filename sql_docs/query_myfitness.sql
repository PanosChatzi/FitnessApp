USE [myFitnessApp]
SELECT DB_NAME() AS CurrentDatabase
GO

SELECT * FROM [dbo].[FitnessData]
ORDER BY Date DESC
go

DELETE FROM FitnessData 
WHERE ActivityId = 12393571816;
GO

DELETE FROM FitnessData
WHERE ActivityID = 12367487064
GO

EXEC sp_columns @table_name = 'FitnessData';
go

DROP TABLE FitnessData
go

DELETE FitnessData