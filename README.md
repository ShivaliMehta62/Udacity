# Data Modeling with Postgres

## Content
A startup called Sparkify wants to analyze the data they've been collecting on songs and user activity on their new music streaming app. The analytics team is particularly interested in understanding what songs users are listening to. Currently, they don't have an easy way to query their data, which resides in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app.

They'd like a data engineer to create a Postgres database with tables designed to optimize queries on song play analysis, and bring you on the project. Your role is to create a database schema and ETL pipeline for this analysis. You'll be able to test your database and ETL pipeline by running queries given to you by the analytics team from Sparkify and compare your results with their expected results.

## Project Description
In this project, you'll apply what you've learned on data modeling with Postgres and build an ETL pipeline using Python. To complete the project, you will need to define fact and dimension tables for a star schema for a particular analytic focus, and write an ETL pipeline that transfers data from files in two local directories into these tables in Postgres using Python and SQL.

## Data Model
The schema used in this project is STAR Schema. 
The tables are:

## Fact Table: 

#### SONGPLAYS
- songplay_id (INT) PRIMARY KEY
- start_time (DATE) NOT NULL
- user_id (INT) NOT NULL
- level (TEXT)
- song_id (TEXT) NOT NULL
- artist_id (TEXT) NOT NULL
- session_id (INT)
- location (TEXT)
- user_agent (TEXT)

## Dimension Tables:

#### Users 

- user_id (INT) PRIMARY KEY
- first_name (TEXT) NOT NULL
- last_name (TEXT) NOT NULL
- gender (TEXT)
- level (TEXT)

#### Songs 

- song_id (TEXT) PRIMARY KEY
- title (TEXT) NOT NULL
- artist_id (TEXT) NOT NULL
- year (INT)
- duration (FLOAT) NOT NULL

#### Artists 

- artist_id (TEXT) PRIMARY KEY
- name (TEXT) NOT NULL
- location (TEXT)
- lattitude (FLOAT)
- longitude (FLOAT)

#### Time 

- start_time (DATE) PRIMARY KEY
- hour (INT)
- day (INT)
- week (INT)
- month (INT)
- year (INT)
- weekday (TEXT)

## Project Structure

Files used in project-
1. **Data**  folder nested at the home of the project, where all needed jsons reside.
2. **sql_queries.py** contains all your sql queries, and is imported into the files bellow.
3. **create_tables.py** drops and creates tables. You run this file to reset your tables before each time you run your ETL scripts.
4. **test.ipynb** displays the first few rows of each table to let you check your database.
5. **etl.ipynb** reads and processes a single file from song_data and log_data and loads the data into your tables.
6. **etl.py** reads and processes files from song_data and log_data and loads them into your tables.
7. **README.md** current file, provides discussion on this project.

### ETL Pipeline

1. Database and tables created

2. Process Song files
    - Data inserted into **Songs** Table
    - Data inserted into **Artists** Table
  
3. Process Log File
    - Inserting timestamp in **Time** Table
    - Insert user info in **Users** Table
    - Insert songplay records into **Songplays** Table. Here we require, song_id and artist_id. This is an integral part of the Star Schema being followed inthis porject.

4. Disconnect the connection.



  


