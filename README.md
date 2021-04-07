## COVID19-Dashboard

An interactive dashboard for COVID-19 on Amazon EC2.

The dataset used is weekly data from EU open data portal: https://data.europa.eu/euodp/en/data/dataset/covid-19-coronavirus-data

The database is stored on Amazon RDS , and the dashboard is created with Metabase server on AWS machine.

<br><br><br>
<img src="images/dashboard.gif">
<br><br><br>

### Built With:
- Metabase
- PostgreSQL
- Amazon EC2
- Amazon RDS


### Usage:
- Clone the repo.

- with covid_19db.sql file you can upload the database to Amazon RDS with the following command:

  psql -f covid_19db.sql -h 'remote-endpoint' -U 'user' -p 5432 -d 'dbname'
    
  but you should create a database on RDS called: covid_19db , instead you can push the database into your local maschine.
  
- Setup Metabase on Amazon EC2 or instead on your local maschine and connect Metabase with the database.

- you can start creating your own Dashboard, in "corona queries" file, you can find examples of the queries that I have used.

- to update the dashboard, you can execute DB_update.py providing the latest dataset from the site above.

   python DB_update.py 'new_dataset.csv'
   
   but you have to change the database connection information in the file depending on where your database is stored.
    
    
## License

[![License](http://img.shields.io/:license-mit-blue.svg?style=flat-square)](http://badges.mit-license.org)

- **[MIT license](http://opensource.org/licenses/mit-license.php)**

 
