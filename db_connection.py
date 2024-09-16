# db_connection.py

from sqlalchemy import create_engine
from config import SERVER_NAME, DATABASE_NAME

def connect_to_db():
    conn_string = f'mssql+pyodbc://{SERVER_NAME}/{DATABASE_NAME}?driver=ODBC+Driver+17+for+SQL+Server'
    engine = create_engine(conn_string)
    return engine
