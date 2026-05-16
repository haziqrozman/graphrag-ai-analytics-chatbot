/*
================================================================================
Script  : create_mssql_login.sql
Purpose : Creates a SQL Server login, maps it to the DataAnalytics database,
          and assigns db_owner role membership.
================================================================================
*/

-- Create SQL login
CREATE LOGIN username WITH PASSWORD = 'password';

-- Map to database
USE DataAnalytics;  

CREATE USER username FOR LOGIN username;

ALTER ROLE db_owner ADD MEMBER username;