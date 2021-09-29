#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Drop Tables


# In[ ]:


songplay_table_drop = "DROP table IF EXISTS songplays"


# In[ ]:


user_table_drop = "DROP table IF EXISTS users"


# In[ ]:


song_table_drop = "DROP table IF EXISTS songs"


# In[ ]:


artist_table_drop = "DROP table IF EXISTS artists"


# In[ ]:


time_table_drop = "DROP table IF EXISTS time"


# In[ ]:


#Create Tables


# In[ ]:


songplay_table_create ="CREATE TABLE IF NOT EXISTS Songplays(songplay_id int ,start_time date NOT null,user_id int NOT null,                                                                    level text, song_id text, artist_id text, session_id int,                                                                                location text,user_agent text)"


# In[ ]:


user_table_create ="CREATE TABLE IF NOT EXISTS Users(user_id int , first_name text, last_name text, gender text,level text)"                                   


# In[ ]:


song_table_create ="CREATE TABLE IF NOT EXISTS Songs(song_id text , title text, artist_id text, year int,                                                                    duration float)"


# In[ ]:


artist_table_create ="CREATE TABLE IF NOT EXISTS Artists(artist_id text ,name text, location text,                                                                     latitude float, longitude decimal)"


# In[ ]:


time_table_create ="CREATE TABLE IF NOT EXISTS Time(start_time date ,hour int,day int,week int,month int,year int,                                                                 weekday text)"


# In[ ]:


#Insert rows


# In[ ]:


songplay_table_insert="INSERT INTO Songplays VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)"


# In[ ]:


user_table_insert="INSERT INTO Users VALUES(%s,%s,%s,%s,%s)"


# In[ ]:


song_table_insert="INSERT INTO Songs VALUES(%s,%s,%s,%s,%s)"


# In[ ]:


artist_table_insert="INSERT INTO Artists VALUES(%s,%s,%s,%s,%s)"


# In[ ]:


time_table_insert="INSERT INTO Time VALUES(%s,%s,%s,%s,%s,%s,%s)"


# In[ ]:


#Find Songs


# In[ ]:


song_select = """SELECT a.song_id, b.artist_id FROM songs a JOIN artists b ON (a.artist_id = b.artist_id) WHERE a.title = %s AND b.name = %s AND a.duration = %s"""


# In[ ]:


#QueryList


# In[ ]:


create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]


# In[ ]:


drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]


# In[ ]:



