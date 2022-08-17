import pandas as pd
import json

def json_to_dataframe(response_str, response):
    if (response_str == 'response_countries'):
        initial_json = list(response.json()['data'].values())
        medium_json = json.dumps(initial_json)
        df = pd.read_json(medium_json)
        return df
    elif (response_str == 'response_seasons'):
        initial_json = response.json()['data']
        medium_json = json.dumps(initial_json)
        df = pd.read_json(medium_json)
        return df
    elif ((response_str == 'response_teams') or (response_str == 'response_players')):
        initial_json = pd.json_normalize(response.json()['data'], sep='_')
        medium_m_json = initial_json.to_dict(orient='records')
        medium_json = json.dumps(medium_m_json)
        df = pd.read_json(medium_json)
        return df
    else:
        initial_json = pd.json_normalize(
            response.json()['data']['standings'], sep='_')
        medium_m_json = initial_json.to_dict(orient='records')
        medium_json = json.dumps(medium_m_json)
        df = pd.read_json(medium_json)
        return df
