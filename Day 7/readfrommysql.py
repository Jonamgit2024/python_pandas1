# import pip
# pip install ipython-sql
# pip install psycopg2-binary
# pip install sqlalchemy 
# pip install pymysql
# pip install cryptography

import pandas as pd
from sqlalchemy import create_engine

username = 'itversity_retail_user'
password = 'itversity'
host = 'localhost'
port = 3306
database = 'itversity_retail_db'

conn_url = f'mysql+pymysql://{username}:{password}@{host}:{port}/{database}'

def readingfrommysql(url_connection):
    engine = create_engine(url_connection)
    try:
        query = "SELECT * FROM orders WHERE order_status NOT IN ('CLOSED', 'COMPLETE');"  # Corrected query
        df = pd.read_sql(query, engine)
        print(df)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if 'engine' in locals():
            engine.dispose()

readingfrommysql(conn_url)