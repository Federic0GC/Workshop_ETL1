import os
import pandas as pd
from sqlalchemy import create_engine
from Workshop_csv import candidates_df
from dotenv import load_dotenv
import pymysql


load_dotenv()


db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_host = os.getenv("DB_HOST")
db_database = os.getenv("DB_DATABASE")


Workshop_1_mysql_connection = pymysql.connect(db=db_database, user=db_user, passwd=db_password)

try:
    
    Workshop_1_mysql_connection_str = f'mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_database}'

    Workshop_1_mysql_db_connection = create_engine(Workshop_1_mysql_connection_str)
    print("Connection made to the database...")

    candidates_df.to_sql('candidates', con=Workshop_1_mysql_db_connection, index=False, if_exists='replace')
    print("Data loaded correctly in the 'candidates' table'")
    print("Check if the table was successfully added to your database (MySQL)")

except pymysql.Error as e:
    
    print(f"Failed to connect to MYSQL database: {e}")

finally:
    
    if 'workshop_1_mysql_db_connection' in locals():
        Workshop_1_mysql_db_connection.dispose()
    print("Data connection and upload done correctly, connection closed")

    
