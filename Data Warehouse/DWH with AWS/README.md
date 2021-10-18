# Data Warehouse

## Content
A music streaming startup, Sparkify, has grown their user base and song database and want to move their processes and data onto the cloud. Their data resides in S3, in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app.

They'd like a data engineer to build an ETL pipeline that extracts their data from S3, stages them in Redshift, and transforms data into a set of dimensional tables for their analytics team to continue finding insights in what songs their users are listening to. You'll be able to test your database and ETL pipeline by running queries given to you by the analytics team from Sparkify and compare your results with their expected results.

## Project Description
In this project, you'll apply what you've learned on data warehouses and AWS to build an ETL pipeline for a database hosted on Redshift. To complete the project, you will need to load data from S3 to staging tables on Redshift and execute SQL statements that create the analytics tables from these staging tables.

## Fact Table: 

#### SONGPLAYS
- songplay_id INTEGER IDENTITY(0,1)   PRIMARY KEY,
- start_time TIMESTAMP NOT NULL SORTKEY DISTKEY,
- user_id INTEGER  NOT null,
- level VARCHAR,
- song_id VARCHAR NOT NULL,
- artist_id VARCHAR NOT NULL,
- session_id INTEGER,
- location VARCHAR,
- user_agent VARCHAR

## Dimension Tables:

#### Users 

- user_id INTEGER NOT NULL SORTKEY PRIMARY KEY,
- first_name VARCHAR NOT NULL,
- last_name VARCHAR NOT NULL,
- gender VARCHAR NOT NULL,
- level VARCHAR NOT NULL

#### Songs 

- song_id VARCHAR NOT NULL SORTKEY PRIMARY KEY,
- title VARCHAR NOT NULL,
- artist_id VARCHAR NOT NULL,
- year INTEGER NOT NULL,
- duration FLOAT

#### Artists 

- artist_id VARCHAR NOT NULL SORTKEY PRIMARY KEY,
- name VARCHAR NOT NULL,
- location VARCHAR,
- latitude FLOAT,
- longitude FLOAT

#### Time 

- start_time TIMESTAMP NOT NULL DISTKEY SORTKEY PRIMARY KEY,
- hour INTEGER NOT NULL,
- day INTEGER NOT NULL,
- week INTEGER NOT NULL,
- month INTEGER NOT NULL,
- year INTEGER NOT NULL,
- weekday VARCHAR(20) NOT NULL

## Project Structure

### Creating Table Schema

1. **sql_queries.py** contains all sql queries, and is imported into the files below.
3. **create_tables.py** drops and creates tables. You run this file to reset your tables each time before you run ETL scripts.
4. Launch Redshift cluster and create an IAM role that connects to s3 bucket.
5. **dwh.cfg** contains the Redshift cluster and IAM role information.

### ETL Pipeline

1. **etl.py** contains the logic to load data from s3 bucket to staging tables in Redshift and then from staging table to analytical tables in      Redshift. 

2. load_staging_tables
    - Data inserted into **Staging** tables (staging_events_copy,staging_songs_copy)
  
3. insert_tables
    - Data inserted into **Analytical** tables (songplay, user, song, artist, time)

4. Delete the redshift cluster.


## How to Run

1. Create an IAM User Role, Assign appropriate permissions and create the Redshift Cluster.  
2. Now add the Redshift database and IAM role related info to **dwh.cfg** file.
3. Create python environment with all th required dependencies.
4. Run the below script in terminal for droping and creating tables
    <mark>python create_tables.py</mark>
5. Run the below script in terminal to perform ETL process
    <mark>python etl.py</mark>
6. Check everything is wokring fine.    
7. Delete the redshift cluster,IAM role and assigned permissions.    


  


