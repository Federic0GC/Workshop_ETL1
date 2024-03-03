import pandas as pd
import os
from sqlalchemy import create_engine
from dotenv import load_dotenv
import pymysql

load_dotenv()

db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_host = os.getenv("DB_HOST")
db_database = os.getenv("DB_DATABASE")

Workshop_querys_mysql_connection = pymysql.connect(db=db_database, user=db_user, passwd=db_password)

try:
    Workshop_querys_mysql_connection_str = f'mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_database}'
    Workshop_querys_mysql_db_connection = create_engine(Workshop_querys_mysql_connection_str)

    candidates_select_all_data_sql_query = "SELECT * FROM candidates"
    candidates_df = pd.read_sql_query(candidates_select_all_data_sql_query, Workshop_querys_mysql_db_connection)

    candidates_df['Hired'] = candidates_df.apply(lambda row: 'Yes' if row['Technical Interview Score'] >= 7 and row['Code Challenge Score'] >= 7 else 'No', axis=1)

    code_challenge_aprobados_df = candidates_df[candidates_df['Code Challenge Score'] >= 7] 
    print(f"Number of records with Code Challenge Score >= 7: {len(code_challenge_aprobados_df)}")

    technical_interview_aprobados_df = candidates_df[candidates_df['Technical Interview Score'] >= 7] 
    print(f"Number of records with Technical Interview Score >= 7: {len(technical_interview_aprobados_df)}")

    candidates_show_tables_sql_query = "SHOW TABLES;"
    tabla_df = pd.read_sql_query(candidates_show_tables_sql_query, Workshop_querys_mysql_db_connection)
    print("These are the tables that the database has right now:")
    print(tabla_df)

    candidates_hired = 'candidates_hired'
    candidates_df.to_sql(candidates_hired, Workshop_querys_mysql_db_connection, index=False, if_exists='replace')

    print(f"Data loaded correctly in the table '{candidates_hired}'.")

    sql_query_hired = f"SELECT * FROM {candidates_hired}"
    candidates_hired_df = pd.read_sql_query(sql_query_hired, Workshop_querys_mysql_db_connection)
    print("New DataFrame with the 'Hired' field:")
    print(candidates_hired_df.head())

except pymysql.Error as e:
    print(f"Failed to connect to MYSQL database: {e}")

finally:
    if 'Workshop_querys_mysql_db_connection' in locals():
        Workshop_querys_mysql_db_connection.dispose()
        print("Creation of the new table with the field 'Hired', and other queries performed successfully, closing the new connection...")
