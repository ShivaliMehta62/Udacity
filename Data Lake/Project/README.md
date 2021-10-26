# Data Lake

## Content
A music streaming startup, Sparkify, has grown their user base and song database and want to move their processes and data onto the cloud. Their data resides in S3, in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app.

They'd like a data engineer to build an ETL pipeline that extracts their data from S3, processes them using Spark, and loads the data back into S3 as a set of dimensional tables. This will allow their analytics team to continue finding insights in what songs their users are listening to.You'll be able to test your database and ETL pipeline by running queries given to you by the analytics team from Sparkify and compare your results with their expected results.


## Project Description
In this project, you'll apply what you've learned on Spark and data lakes to build an ETL pipeline for a data lake hosted on S3. To complete the project, you will need to load data from S3, process the data into analytics tables using Spark, and load them back into S3. You'll deploy this Spark process on a cluster using AWS.

## Fact Table: 

#### SONGPLAYS
- songplay_id INTEGER IDENTITY(0,1)   PRIMARY KEY,
- start_time TIMESTAMP NOT NULL SORTKEY DISTKEY,
- user_id INTEGER  NOT null,
- level TEXT,
- song_id TEXT NOT NULL,
- artist_id TEXT NOT NULL,
- session_id INTEGER,
- location TEXT,
- user_agent TEXT

## Dimension Tables:

#### Users 

- user_id INTEGER NOT NULL ,
- first_name TEXT NOT NULL,
- last_name TEXT NOT NULL,
- gender TEXT NOT NULL,
- level TEXT NOT NULL

#### Songs 

- song_id TEXT NOT NULL ,
- title TEXT NOT NULL,
- artist_id TEXT NOT NULL,
- year INTEGER NOT NULL,
- duration FLOAT

#### Artists 

- artist_id TEXT NOT NULL ,
- name TEXT NOT NULL,
- location TEXT,
- latitude FLOAT,
- longitude FLOAT

#### Time 

- start_time TIMESTAMP NOT NULL ,
- hour INTEGER NOT NULL,
- day INTEGER NOT NULL,
- week INTEGER NOT NULL,
- month INTEGER NOT NULL,
- year INTEGER NOT NULL,
- weekday TEXT NOT NULL

## How to Run

1. Create a file dl.cfg containing below info:
    <mark>AWS_ACCESS_KEY_ID</mark>
    <mark>AWS_SECRET_ACCESS_KEY</mark>
2. Create S3 bucket where the output will be stored.
3. Finally run **etl.py** in terminal 
    <mark>python etl.py</mark>
    