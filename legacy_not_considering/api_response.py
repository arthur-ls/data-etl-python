from urllib import response
import pip._vendor.requests as req
import pandas as pd
import json
import psycopg2 as ps2
from sqlalchemy import create_engine

headers = {'apikey': API_KEY}
params = (("league_id", "314"),)
params2 = (("continent", "Europe"),)
params3 = (("country_id", "48"),)
params4 = (("season_id", "496"),)

api_url_countries = ENDPOINT_COUNTRIES
api_url_seasons = ENDPOINT_SEASONS
api_url_teams = ENDPOINT_TEAMS
api_url_players = ENDPOINT_PLAYERS
api_url_standings = ENDPOINT_STANDINGS

response_countries = req.get(
    api_url_countries, headers=headers, params=params2)
response_seasons = req.get(api_url_seasons, headers=headers, params=params)
response_teams = req.get(api_url_teams, headers=headers, params=params3)
response_players = req.get(api_url_players, headers=headers, params=params3)
response_standings = req.get(
    api_url_standings, headers=headers, params=params4)

initial_df = list(response_countries.json()['data'].values())
medium_df = json.dumps(initial_df)
df_countries = pd.read_json(medium_df)

initial_df = response_seasons.json()['data']
medium_df = json.dumps(initial_df)
df_seasons = pd.read_json(medium_df)

initial_df = pd.json_normalize(response_teams.json()['data'], sep='_')
medium_dff = initial_df.to_dict(orient='records')
medium_df = json.dumps(medium_dff)
df_teams = pd.read_json(medium_df)

initial_df = pd.json_normalize(response_players.json()['data'], sep='_')
medium_dff = initial_df.to_dict(orient='records')
medium_df = json.dumps(medium_dff)
df_players = pd.read_json(medium_df)

initial_df = pd.json_normalize(response_standings.json()[
                               'data']['standings'], sep='_')
medium_dff = initial_df.to_dict(orient='records')
medium_df = json.dumps(medium_dff)
df_standings = pd.read_json(medium_df)

conn = ps2.connect(
    database="rentx",
    user="docker",
    password="docker",
    host="localhost",
    port="5432")

cur = conn.cursor()

cur.execute(
    '''CREATE TABLE IF NOT EXISTS seasons (
       season_id INT,
       name CHAR(50),
       is_current CHAR(5),
       country_id CHAR(100),
       league_id CHAR(200),
       start_date CHAR(100),
       end_date CHAR(100)
       )'''
)
conn.commit()

cur.execute(
    '''CREATE TABLE IF NOT EXISTS countries (
        id INT, 
        name CHAR(50), 
        country_code CHAR(5),
        continent CHAR(50)
        )'''
)
conn.commit()

cur.execute(
    '''CREATE TABLE IF NOT EXISTS teams (
       team_id INT,
       name CHAR(50),
       short_code CHAR(5),
       logo CHAR(100),
       country_country_id INT,
       country_name CHAR(100),
       country_country_code CHAR(100),
       country_continent CHAR(100)
       )'''
)
conn.commit()

cur.execute(
    '''CREATE TABLE IF NOT EXISTS players (
        player_id INT, 
        firstname CHAR(50), 
        lastname CHAR(50),
        birthday CHAR(50),
        age INT,
        weight FLOAT,
        height FLOAT,
        img CHAR(100),
        country_country_id INT,
        country_name CHAR(100),
        country_country_code CHAR(100),
        country_continent CHAR(100)
        )'''
)
conn.commit()

cur.execute(
    '''CREATE TABLE IF NOT EXISTS standings (
            team_id INT,
            points INT,
            status CHAR(50),
            result CHAR (50),
            overall_games_played INT,
            overall_won INT,
            overall_draw INT,
            overall_lost INT,
            overall_goals_diff INT,
            overall_goals_scored INT,
            overall_goals_against INT,
            home_games_played INT,
            home_won INT,
            home_draw INT,
            home_lost INT,
            home_goals_diff INT,
            home_goals_scored INT,
            home_goals_against INT,
            away_games_played INT,
            away_won INT,
            away_draw INT,
            away_lost INT,
            away_goals_diff INT,
            away_goals_scored INT,
            away_goals_against INT
        )'''
)
conn.commit()

conn_string = 'postgresql://docker:docker@localhost/rentx'

db = create_engine(conn_string)

df_countries.to_sql('countries', con=db, if_exists='replace', index=False)
df_seasons.to_sql('seasons', con=db, if_exists='replace', index=False)
df_teams.to_sql('teams', con=db, if_exists='replace', index=False)
df_players.to_sql('players', con=db, if_exists='replace', index=False)
df_standings.to_sql('standings', con=db, if_exists='replace', index=False)

conn.commit()
