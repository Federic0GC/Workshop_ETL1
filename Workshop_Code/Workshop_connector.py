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


mysql_connection = pymysql.connect(db=db_database, user=db_user, passwd=db_password)

try:
    
    mysql_connection_str = f'mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_database}'

    mysql_db_connection = create_engine(mysql_connection_str)
    print("Conexion hecha con la base de datos")

    candidates_df.to_sql('candidates', con=mysql_db_connection, index=False, if_exists='replace')
    print("Datos cargados correctamente en la tabla 'candidates'.")

except pymysql.Error as e:
    
    print(f"Error al conectar a la base de datos MySQL: {e}")

finally:
    
    if 'mysql_db_connection' in locals():
        mysql_db_connection.dispose()
