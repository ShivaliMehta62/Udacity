import configparser


# CONFIG
config = configparser.ConfigParser()
config.read('dwh.cfg')

# GLOBAL VARIABLES
LOG_DATA = config.get("S3","LOG_DATA")
LOG_PATH = config.get("S3", "LOG_JSONPATH")
SONG_DATA = config.get("S3", "SONG_DATA")
IAM_ROLE = config.get("IAM_ROLE","ARN")

# DROP TABLES

staging_events_table_drop = "DROP table IF EXISTS staging_events"
staging_songs_table_drop = "DROP table IF EXISTS staging_songs"
songplay_table_drop = "DROP table IF EXISTS songplays"
user_table_drop = "DROP table IF EXISTS users"
song_table_drop = "DROP table IF EXISTS songs"
artist_table_drop = "DROP table IF EXISTS artists"
time_table_drop = "DROP table IF EXISTS time"

# CREATE TABLES

staging_events_table_create= ("""
    CREATE TABLE IF NOT EXISTS staging_events(
        artist VARCHAR,
        auth VARCHAR,
        firstName VARCHAR,
        gender VARCHAR,
        itemInSession INTEGER,
        lastName VARCHAR,
        length FLOAT,
        level VARCHAR,
        location VARCHAR,
        method VARCHAR,
        page VARCHAR,
        registration FLOAT,
        sessionId INTEGER,
        song VARCHAR,
        status INTEGER,
        ts TIMESTAMP,
        userAgent VARCHAR,
        userId INTEGER 
        )
""")

staging_songs_table_create = ("""
    CREATE TABLE IF NOT EXISTS staging_songs(
        num_songs INTEGER,
        artist_id VARCHAR,
        artist_latitude FLOAT,
        artist_longitude FLOAT,
        artist_location VARCHAR,
        artist_name VARCHAR,
        song_id VARCHAR,
        title VARCHAR,
        duration FLOAT,
        year INTEGER
    )
""")

songplay_table_create = ("""
     CREATE TABLE IF NOT EXISTS Songplays(
        songplay_id INTEGER IDENTITY(0,1)   PRIMARY KEY,
        start_time TIMESTAMP NOT NULL SORTKEY DISTKEY,
        user_id INTEGER  NOT null,
        level VARCHAR,
        song_id VARCHAR NOT NULL,
        artist_id VARCHAR NOT NULL,
        session_id INTEGER,
        location VARCHAR,
        user_agent VARCHAR
    )
""")

user_table_create = ("""
    CREATE TABLE users(
        user_id INTEGER NOT NULL SORTKEY PRIMARY KEY,
        first_name VARCHAR NOT NULL,
        last_name VARCHAR NOT NULL,
        gender VARCHAR NOT NULL,
        level VARCHAR NOT NULL
    )
""")

song_table_create = ("""
    CREATE TABLE songs(
        song_id VARCHAR NOT NULL SORTKEY PRIMARY KEY,
        title VARCHAR NOT NULL,
        artist_id VARCHAR NOT NULL,
        year INTEGER NOT NULL,
        duration FLOAT
    )
""")

artist_table_create = ("""
    CREATE TABLE artists(
        artist_id VARCHAR NOT NULL SORTKEY PRIMARY KEY,
        name VARCHAR NOT NULL,
        location VARCHAR,
        latitude FLOAT,
        longitude FLOAT
    )
""")

time_table_create = ("""
    CREATE TABLE time(
        start_time TIMESTAMP NOT NULL DISTKEY SORTKEY PRIMARY KEY,
        hour INTEGER NOT NULL,
        day INTEGER NOT NULL,
        week INTEGER NOT NULL,
        month INTEGER NOT NULL,
        year INTEGER NOT NULL,
        weekday VARCHAR(20) NOT NULL
    )
""")

# STAGING TABLES

staging_events_copy = ("""
    copy staging_events from {}
    credentials 'aws_iam_role={}'
    compupdate off region 'us-west-2' 
    timeformat as 'epochmillisecs'
    format as JSON {};
""").format(LOG_DATA,IAM_ROLE,LOG_PATH)

staging_songs_copy = ("""
    copy staging_songs from {}
    credentials 'aws_iam_role={}'
    compupdate off region 'us-west-2' 
    format as JSON 'auto';
""").format(SONG_DATA, IAM_ROLE)

# FINAL TABLES

songplay_table_insert = ("""
    INSERT INTO songplays (start_time, user_id, level, song_id, artist_id, session_id, location, user_agent)
    SELECT  DISTINCT to_timestamp(to_char(e.ts, '9999-99-99 99:99:99'),'YYYY-MM-DD HH24:MI:SS') , 
            e.userId        AS user_id, 
            e.level         AS level, 
            s.song_id       AS song_id, 
            s.artist_id     AS artist_id, 
            e.sessionId     AS session_id, 
            e.location      AS location, 
            e.userAgent     AS user_agent
    FROM staging_events e
    JOIN staging_songs s ON e.song = s.title AND e.artist = s.artist_name;
""")

user_table_insert = ("""
    INSERT INTO users (user_id, first_name, last_name, gender, level)
    SELECT  DISTINCT(userId) AS user_id,
            firstName AS first_name,
            lastName AS last_name,
            gender,
            level
    FROM staging_events
    WHERE user_id IS NOT NULL;
""")

song_table_insert = ("""
    INSERT INTO songs (song_id, title, artist_id, year, duration)
    SELECT  DISTINCT(song_id) AS song_id,
            title,
            artist_id,
            year,
            duration
    FROM staging_songs
    WHERE song_id IS NOT NULL;
""")

artist_table_insert = ("""
    INSERT INTO artists (artist_id, name, location, latitude, longitude)
    SELECT  DISTINCT(artist_id) AS artist_id,
            artist_name  AS name,
            artist_location AS location,
            artist_latitude AS latitude,
            artist_longitude AS longitude
    FROM staging_songs
    WHERE artist_id IS NOT NULL;
""")

time_table_insert = ("""
    INSERT INTO time (start_time, hour, day, week, month, year, weekday)
    SELECT  DISTINCT(ts) AS start_time,
            EXTRACT(hour FROM ts) AS hour,
            EXTRACT(day FROM ts)  AS day,
            EXTRACT(week FROM ts)  AS week,
            EXTRACT(month FROM ts) AS month,
            EXTRACT(year FROM ts) AS year,
            EXTRACT(dayofweek FROM ts)  AS weekday
    FROM staging_events;
""")

# QUERY LISTS

create_table_queries = [staging_events_table_create, staging_songs_table_create, songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [staging_events_table_drop, staging_songs_table_drop, songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
copy_table_queries = [staging_events_copy, staging_songs_copy]
insert_table_queries = [songplay_table_insert, user_table_insert, song_table_insert, artist_table_insert, time_table_insert]
