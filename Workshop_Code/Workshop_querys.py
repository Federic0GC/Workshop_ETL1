import pandas as pd
from sqlalchemy import create_engine
from Workshop_connector import mysql_db_connection


sql_query = "SELECT * FROM candidates"
candidates_df = pd.read_sql_query(sql_query, mysql_db_connection)


candidates_df['Hired'] = candidates_df.apply(lambda row: 'Yes' if row['Technical Interview Score'] >= 7 and row['Code Challenge Score'] >= 7 else 'No', axis=1)

code_challenge_aprobados_df = candidates_df[candidates_df['Code Challenge Score'] >= 7] 
print(f"Cantidad de registros con Code Challenge Score >= 7: {len(code_challenge_aprobados_df)}")

technical_interview_aprobados_df = candidates_df[candidates_df['Technical Interview Score'] >= 7] 
print(f"Cantidad de registros con Technical Interview Score >= 7: {len(technical_interview_aprobados_df)}")

sql_query_tables = "SHOW TABLES;"
tabla_df = pd.read_sql_query(sql_query_tables, mysql_db_connection)
print("Lista de tablas en la base de datos:")
print(tabla_df)

candidates_hired = 'candidates_hired'
candidates_df.to_sql(candidates_hired, mysql_db_connection, index=False, if_exists='replace')

print(f"Datos cargados correctamente en la tabla '{candidates_hired}'.")

sql_query_hired = f"SELECT * FROM {candidates_hired}"
candidates_hired_df = pd.read_sql_query(sql_query_hired, mysql_db_connection)
print("Nuevo DataFrame con el campo 'Hired':")
print(candidates_hired_df.head())

mysql_db_connection.dispose()
