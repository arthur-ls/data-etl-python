from urllib import response
import pip._vendor.requests as req
import pandas as pd
import json
import psycopg2 as ps2
from sqlalchemy import create_engine


def connect_db(db, user, pwd, host, port):
    conn = ps2.connect(
        database=db,
        user=user,
        password=pwd,
        host=host,
        port=port)
    return conn


def exec_query(connection, query):
    cur = connection.cursor()
    cur.execute(query)
    connection.commit()


def insert_db(connection, df, table_name, engine_connection_string):
    df.to_sql(table_name, con=engine_connection_string,
              if_exists='replace', index=False)
    connection.commit()
