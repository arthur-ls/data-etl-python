
from sqlalchemy import create_engine
from services import service
from api import api
from database import database, queries
import os
import resources
from urllib import response
import pip._vendor.requests as req
import pandas as pd
import json
import psycopg2 as ps2
from dotenv import load_dotenv


def main():
    load_dotenv("/home/arthu/data-ingestion-python/resources/parameters.env")
    headers = {'apikey': os.getenv('API_KEY')}
    params = (("league_id", "314"),)
    params2 = (("continent", "Europe"),)
    params3 = (("country_id", "48"),)
    params4 = (("season_id", "496"),)
    conn_string = f"postgresql://{os.getenv('PG_USER')}:{os.getenv('PG_PWD')}@{os.getenv('PG_HOST')}/{os.getenv('PG_DB')}"
    db = create_engine(conn_string)

    # requests from api #
    response_countries = api.get_api_data(os.getenv('API_URL_COUNTRIES'),
                                          headers, params2)
    response_seasons = api.get_api_data(os.getenv('API_URL_SEASONS'),
                                        headers, params)
    response_teams = api.get_api_data(os.getenv('API_URL_TEAMS'),
                                      headers, params3)
    response_players = api.get_api_data(os.getenv('API_URL_PLAYERS'),
                                        headers, params3)
    response_standings = api.get_api_data(os.getenv('API_URL_STANDINGS'),
                                          headers, params4)

    # creating dataframe from json #
    df_countries = service.json_to_dataframe(
        'response_countries', response_countries)
    df_seasons = service.json_to_dataframe(
        'response_seasons', response_seasons)
    df_teams = service.json_to_dataframe('response_teams', response_teams)
    df_players = service.json_to_dataframe(
        'response_players', response_players)
    df_standings = service.json_to_dataframe(
        'response_standings', response_standings)

    # connection string #
    conn = database.connect_db(os.getenv('PG_DB'), os.getenv('PG_USER'), os.getenv(
        'PG_PWD'), os.getenv('PG_HOST'), os.getenv('PG_PORT'))

    # creating tables in database #
    database.exec_query(conn, queries.create_table_countries)
    database.exec_query(conn, queries.create_table_seasons)
    database.exec_query(conn, queries.create_table_teams)
    database.exec_query(conn, queries.create_table_players)
    database.exec_query(conn, queries.create_table_standings)

    # inserting dataframe in database tables #
    database.insert_db(conn, df_countries, 'countries', db)
    database.insert_db(conn, df_seasons, 'seasons', db)
    database.insert_db(conn, df_teams, 'teams', db)
    database.insert_db(conn, df_players, 'players', db)
    database.insert_db(conn, df_standings, 'standings', db)


if __name__ == "__main__":
    main()
