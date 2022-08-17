create_table_seasons = '''CREATE TABLE IF NOT EXISTS seasons (
                            season_id INT,
                            name CHAR(50),
                            is_current CHAR(5),
                            country_id CHAR(100),
                            league_id CHAR(200),
                            start_date CHAR(100),
                            end_date CHAR(100)
                            )'''

create_table_countries = '''CREATE TABLE IF NOT EXISTS countries (
                            id INT, 
                            name CHAR(50), 
                            country_code CHAR(5),
                            continent CHAR(50)
                            )'''

create_table_teams = '''CREATE TABLE IF NOT EXISTS teams (
                        team_id INT,
                        name CHAR(50),
                        short_code CHAR(5),
                        logo CHAR(100),
                        country_country_id INT,
                        country_name CHAR(100),
                        country_country_code CHAR(100),
                        country_continent CHAR(100)
                        )'''

create_table_players = '''CREATE TABLE IF NOT EXISTS players (
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

create_table_standings = '''CREATE TABLE IF NOT EXISTS standings (
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
