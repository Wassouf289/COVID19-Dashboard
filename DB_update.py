import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy import String, DateTime,Float, Integer
import argparse
import os

""" get Corona datasets from here
https://data.europa.eu/euodp/en/data/dataset/covid-19-coronavirus-data
"""

def DB_update(csv_file):
    #read data as csv into a pandas dataframe
    df=pd.read_csv(csv_file)

    #change names for easy interept 
    df.columns=['daterep','year_week','cases_weekly','deaths_weekly','country','geographicId','countrycode','population','continent','notification_rate_per_100000_population_14_days']
    df['daterep']=pd.to_datetime(df['daterep'],format ='%d/%m/%Y')
    #connection string details
    HOST = 'postgresdbinstance.ctk9165nwoff.eu-central-1.rds.amazonaws.com'
    PORT = '5432'
    USERNAME = 'postgres'
    PASSWORD = os.getenv('DB_password')
    DB = 'covid_19db'

    conn_string=f'postgres://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DB}'

    #create engine with the connection to the remore DB
    engine=create_engine(conn_string)

    #convert the dataframe to SQL table
    df.to_sql('weekly_cases',con=engine,index=False,if_exists='replace',dtype={
        'dateRep':DateTime() ,
        'year_week':String(),
        'cases_weekly':Integer(),
        'deaths_weekly' :Integer(),
        'country' :String() ,
        'geographicId':String(),
        'countryCode':String(),
        'population': Integer(),
        'continent':String(),
        'notification_rate_per_100000_population_14_days':Float()
        
    })


parser=argparse.ArgumentParser(description='This program updates Corona DB on Amazon RDS')
parser.add_argument('csv_file',help='give the path to csv file')
args=parser.parse_args()
DB_update(args.csv_file)
print('Database updated')

