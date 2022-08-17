# Data ETL Python

## Summary
In this project I created a data pipeline that gets data from SportsDataAPI, transform the data and load it in PostgreSQL that is up due to Docker.


## Methodology
For this project, I used Python for the entire process from data extraction to data load.
I used the requests python lib to GET SportsDataAPI data, besides ```json``` and ```pandas``` to transform data captured in the API, in addition to ```psycopg2``` and ```sqlalchemy``` to connect to PostgreSQL and run the queries.
I also used environment variables to store links and keys that make the connection with the database and API.
Finally, I used Docker to upload a PostgreSQL image and be able to store data.
The tables database are:

The database structure is close to snowflake, since the fact table would be ```standings``` that shows all the team games.

## How to Run
### Docker
First of all, you need Docker installed in your machine. If you are using Windows, the best way to download Docker is using WSL.
After you have installed Docker, you need a PostgreSQL image an replace it in ```docker-compose.yml``` and run ```docker-compose up``` to have your database up.
At last, try to connect to the database using Dbeaver, DataGrip or similar tools. If everything is working, we can move to the next step.
### Endpoints and Keys
You will need to go to [SportsDataAPI](https://app.sportdataapi.com), subscribe and get the endpoints and key you want.
### Running
Finally, with the previous steps done and working you have to go to the terminal and run ```python3 main.py```. Then you will have your database loaded with tables to make queries and get insights
