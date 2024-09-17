# Fitness App

Welcome to the Fitness Database ETL Pipeline! This pipeline is designed to extract workout data files from Intervals.icu, transform the data and load it into a Microsoft SQL database using Python.

## Project Structure

FitnessDatabase # Project folder
│ 
├── etl_pipeline.py # Main ETL script 
├── db_connection.py # Database connection script
├── config.py # Configuration for folder paths and database settings
├── data/ # Folder containing downloaded workout data in CSV format
│ └── i123456_activities.csv # Example CSV file 
├── sql_docs # Folder containing SQL code to create the database
├── README.md # Documentation
├── requirements.txt # Python dependencies

## Dependencies

- Python 3.x
- pandas
- sqlalchemy
- pyodbc
- SQL Server
- Git (optional)

Install dependencies via pip:

```bash
pip install -r requirements.txt
```

## Explanation of Each Folder/File:
1. data/ folder:
    - This is where you will place your CSV files, downloaded from Intervals.icu or other fitness apps.
    - Each file should be named in the format i______activities.csv (e.g., i123456_activities.csv).
    - This folder will serve as the source for your ETL script to find and process the data.

2. etl_pipeline.py:
    - This is your main Python script that handles the ETL process (Extract, Transform, Load).
    - It will scan the data/ folder for new CSV files, transform the data, and load it into your SQL Server database.

3. db_connection.py (optional):
    - You can move your database connection logic to a separate file to keep things modular.
    - This will help separate concerns: one script focuses on database connections, while etl_pipeline.py focuses on the ETL logic.

4. config.py (optional):
    - This can store configuration values like your SQL Server name, database name, and file path constants.
    - It’s useful to avoid hardcoding values in your main script.

5. sql_docs (optional)
    - This is where to store the sql documents to create and query the database.

6. README.md:
    - This file explains what your project does, how to set it up, and how to run the ETL pipeline.
    - It's helpful for future reference or for others who might work with your project.

7. requirements.txt:
    - List all Python dependencies here so that the environment can be easily replicated.

## Configuration
1. Clone the repository to your local machine.
2. Make sure you have Python and the required dependencies installed.
3. Set up a Microsoft SQL database.
4. Configure the connection details. Make sure to replace the DESKTOP-CFN92PN\\MSSQLSERVER2 and myFitnessApp with your own server and database name in the `config.py` file and replace driver=ODBC+Driver+17+for+SQL+Server with your own driver in the `db_connection.py` file.

## Running the pipeline
1. Place your fitness activity CSV files in the data/ folder. These files should follow the naming convention iXXXXXX_activities.csv where XXXXXX is a 6-digit number representing the athlete ID.
2. Run the ETL process by executing etl_pipeline.py.

The pipeline will:
- Extract data from CSV files.
- Transform the data (convert time, distance, and pace).
- Load the data into the FitnessData table in SQL Server.

## Troubleshooting
A common error that you may encounter: "Error occurred while inserting data: (pyodbc.ProgrammingError) ...".

Make sure that the data types in your SQL table match the ones used in the CSV file and Python code. For example, ensure that the Pace column in SQL Server is set to store strings if you're saving it as 'min:sec/km'.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.