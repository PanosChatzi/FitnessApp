# etl_pipeline.py

import os
import pandas as pd
from sqlalchemy.exc import SQLAlchemyError
from db_connection import connect_to_db
from config import DATA_FOLDER

# Extract step: Read the CSV file
def extract_data(file_path):
    df = pd.read_csv(file_path)
    print(f"Data extracted successfully from {file_path}.")
    return df

# Function to format pace
def convert_pace(speed_m_per_s):
    """
    Convert speed in meters per second (m/s) to pace in min:sec/km.

    Args:
    speed_m_per_s (float): Speed in meters per second.

    Returns:
    str: Pace in the format 'min:sec/km'.
    """
    # Convert speed from meters per second to kilometers per minute
    speed_km_per_min = speed_m_per_s * 60 / 1000  # (m/s * 60) / 1000 = km/min

    # Convert speed (km/min) to time per km (minutes per km)
    minutes_per_km = 1 / speed_km_per_min

    # Get the integer part of the minutes
    minutes = int(minutes_per_km)

    # Get the remaining seconds (fractional part converted to seconds)
    seconds = (minutes_per_km - minutes) * 60
    seconds = round(seconds)  # Round to the nearest second

    # Handle case when rounding seconds goes to 60
    if seconds == 60:
        minutes += 1
        seconds = 0

    # Format the output as 'min:sec/km'
    return f"{minutes}:{seconds:02d}/km"

# Transform step
def transform_data(df, athlete_id):
    # Convert time from seconds to minutes
    df['Moving Time'] = df['Moving Time'] / 60
    df['Elapsed time'] = df['Elapsed time'] / 60
    
    # Convert distance from meters to kilometers
    df['Distance'] = df['Distance'] / 1000
    
    # Calculate pace using the new function
    df['Pace'] = df['Pace'].apply(lambda x: convert_pace(x))

    # Round specific columns
    df['Intensity'] = df['Intensity'].round(1)
    df['Avg Altitude'] = df['Avg Altitude'].round(1)
    df['Avg HR%'] = df['Avg HR%'].round(1)
    df['Max HR%'] = df['Max HR%'].round(1)
    df['Max Altitude'] = df['Max Altitude'].round(1)
    df['Pace'] = df['Pace'].round(2)
    df['Distance'] = df['Distance'].round(2)
    df['Moving Time'] = df['Moving Time'].round(2)
    df['Elapsed time'] = df['Elapsed time'].round(2)
    
    # Add athlete_id column
    df['athlete_id'] = athlete_id
    # print extracted data
    print(f"Transformed data for athlete {athlete_id}.")

    # Rename columns to match SQL Server table
    df.rename(columns={
        'athlete_id': 'AthleteId',
        'id': 'ActivityId',
        'Intensity': 'IntensityPercent',
        'Moving Time': 'MovingTime',
        'Elapsed time': 'ElapsedTime',
        'Avg Altitude': 'AvgAltitude',
        'Avg HR%': 'AvgHRPercent',
        'Max HR%': 'MaxHRPercent',
        'Max Altitude': 'MaxAltitude',
        'Max HR': 'MaxHR',
        'HRRc': 'HRRc',  # Assuming 'HRRc' is correct, make sure it's not different in the table
        'Avg HR': 'AvgHR'
    }, inplace=True)
    
    return df

# Load step
def load_data_to_sql(df, engine):
    try:
        df.to_sql('FitnessData', con=engine, if_exists='append', index=False)
        # Print the IDs of activities added
        added_ids = df['ActivityId'].tolist()
        print(f"Activities with the following IDs have been added: {added_ids}")
    except SQLAlchemyError as e:
        print(f"Error occurred while inserting data: {e}")

# Main ETL function
def etl_pipeline():
    engine = connect_to_db()

    for file_name in os.listdir(DATA_FOLDER):
        if file_name.endswith("_activities.csv") and len(file_name) == 22:  # Checking for 6-digit number format
            # Extract the athlete_id from the file name
            athlete_id = file_name.split("_activities")[0]  # This will extract 'i123456' part
            
            file_path = os.path.join(DATA_FOLDER, file_name)
            
            # Extract
            df = extract_data(file_path)
            
            # Transform
            df_transformed = transform_data(df, athlete_id)
            
            # Load
            load_data_to_sql(df_transformed, engine)

# Run the ETL pipeline
if __name__ == "__main__":
    etl_pipeline()
