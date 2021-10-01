#!/usr/bin/env python
# coding: utf-8


#Drop Tables

songplay_table_drop = "DROP table IF EXISTS songplays"
user_table_drop = "DROP table IF EXISTS users"
song_table_drop = "DROP table IF EXISTS songs"
artist_table_drop = "DROP table IF EXISTS artists"
time_table_drop = "DROP table IF EXISTS time"

#Create Tables

songplay_table_create =("""
  CREATE TABLE IF NOT EXISTS Songplays
  (songplay_id SERIAL PRIMARY KEY,
  start_time TIMESTAMP NOT null,
  user_id int NOT null,
  level text,
  song_id text,
  artist_id text,
  session_id int,
  location text,
  user_agent text)
""")

user_table_create =("""
  CREATE TABLE IF NOT EXISTS Users
  (user_id int PRIMARY KEY ,
  first_name text NOT NULL,
  last_name text NOT NULL,
  gender text,
  level text)
  """)                                   


song_table_create =("""
  CREATE TABLE IF NOT EXISTS Songs
  (song_id text PRIMARY KEY ,
  title text NOT NULL,
  artist_id text NOT NULL,
  year int,
  duration float NOT NULL)
  """)


artist_table_create =("""
  CREATE TABLE IF NOT EXISTS Artists
  (artist_id text PRIMARY KEY,
  name text NOT NULL,
  location text,
  latitude float,
  longitude float)
  """)


time_table_create =("""
  CREATE TABLE IF NOT EXISTS Time
  (start_time TIMESTAMP PRIMARY KEY ,
  hour int,
  day int,
  week int,
  month int,
  year int,
  weekday text)
  """)


#Insert rows

songplay_table_insert=("""
  INSERT INTO Songplays 
  (songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent)
  VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s) 
  ON CONFLICT (songplay_id) DO NOTHING
""")

user_table_insert=("""
  INSERT INTO Users
  (user_id, first_name, last_name, gender, level)
  VALUES(%s,%s,%s,%s,%s)
  ON CONFLICT (user_id) DO UPDATE SET level=EXCLUDED.level
""")

song_table_insert=("""
  INSERT INTO Songs
  (song_id, title, artist_id, year, duration)
  VALUES(%s,%s,%s,%s,%s)
  ON CONFLICT(song_id)DO NOTHING
""")  
  
artist_table_insert=("""
  INSERT INTO Artists
  (artist_id, name, location, latitude, longitude)
  VALUES(%s,%s,%s,%s,%s)
  ON CONFLICT(artist_id)DO NOTHING
""")

time_table_insert=("""
  INSERT INTO Time
  (start_time, hour, day, week, month, year, weekday)
  VALUES(%s,%s,%s,%s,%s,%s,%s)
  ON CONFLICT(start_time)DO NOTHING
""")  

#Find Songs

song_select = ("""
SELECT a.song_id, b.artist_id 
FROM songs a JOIN artists b ON (a.artist_id = b.artist_id) 
WHERE a.title = %s AND b.name = %s AND a.duration = %s
""")

#QueryList

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
