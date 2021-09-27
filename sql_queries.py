{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": None,
   "id": "d945bfcc",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Drop Tables"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "id": "e438f798",
   "metadata": {},
   "outputs": [],
   "source": [
    "songplay_table_drop = \"DROP table IF EXISTS songplays\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "id": "c5779cdd",
   "metadata": {},
   "outputs": [],
   "source": [
    "user_table_drop = \"DROP table IF EXISTS users\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "id": "c5ba2c4c",
   "metadata": {},
   "outputs": [],
   "source": [
    "song_table_drop = \"DROP table IF EXISTS songs\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "id": "3dbdc1f7",
   "metadata": {},
   "outputs": [],
   "source": [
    "artist_table_drop = \"DROP table IF EXISTS artists\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "id": "6a57b574",
   "metadata": {},
   "outputs": [],
   "source": [
    "time_table_drop = \"DROP table IF EXISTS time\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "be15b227",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Create Tables"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "id": "51e4c8b9",
   "metadata": {},
   "outputs": [],
   "source": [
    "songplay_table_create =\"CREATE TABLE IF NOT EXISTS Songplays(songplay_id SERIAL PRIMARY KEY,start_time bigint NOT None,user_id int NOT None,\\\n",
    "                                                                level varchar, song_id varchar, artist_id varchar, session_id int, \\\n",
    "                                                                location text,user_agent text)\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "b81c38e0",
   "metadata": {},
   "outputs": [],
   "source": [
    "user_table_create =\"CREATE TABLE IF NOT EXISTS Users(user_id int PRIMARY KEY, first_name varchar, last_name varchar, \\\n",
    "                                                            gender varchar,level varchar)\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "id": "53a8e2f0",
   "metadata": {},
   "outputs": [],
   "source": [
    "song_table_create =\"CREATE TABLE IF NOT EXISTS Songs(song_id varchar PRIMARY KEY, title text, artist_id varchar, year int, \\\n",
    "                                                                duration numeric)\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "id": "149a9018",
   "metadata": {},
   "outputs": [],
   "source": [
    "artist_table_create =\"CREATE TABLE IF NOT EXISTS Artists(artist_id varchar PRIMARY KEY,name varchar, location text, \\\n",
    "                                                                latitude decimal, longitude decimal)\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "id": "277f6d1f",
   "metadata": {},
   "outputs": [],
   "source": [
    "time_table_create =\"CREATE TABLE IF NOT EXISTS Time(start_time bigint PRIMARY KEY,hour int,day int,week int,month int,year int, \\\n",
    "                                                            weekday varchar)\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "id": "ff66b584",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Insert rows"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "id": "0ceee1d1",
   "metadata": {},
   "outputs": [],
   "source": [
    "songplay_table_insert=\"INSERT INTO Songplays VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "id": "e06f174e",
   "metadata": {},
   "outputs": [],
   "source": [
    "user_table_insert=\"INSERT INTO Users VALUES(%s,%s,%s,%s,%s)\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "id": "9549eb83",
   "metadata": {},
   "outputs": [],
   "source": [
    "song_table_insert=\"INSERT INTO Songs VALUES(%s,%s,%s,%s,%s)\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "id": "3fd8cf76",
   "metadata": {},
   "outputs": [],
   "source": [
    "artist_table_insert=\"INSERT INTO Artists VALUES(%s,%s,%s,%s,%s)\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "id": "56f17dbd",
   "metadata": {},
   "outputs": [],
   "source": [
    "time_table_insert=\"INSERT INTO Time VALUES(%s,%s,%s,%s,%s,%s,%s)\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "id": "32f3f282",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Find Songs"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "id": "9165a097",
   "metadata": {},
   "outputs": [],
   "source": [
    "song_select = (\"\"\"select song_id,artist_id from songs a join artists b where a.title=%s and b.name=%s \"\"\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "id": "d8c5a2f8",
   "metadata": {},
   "outputs": [],
   "source": [
    "#QueryList"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "id": "10246e94",
   "metadata": {},
   "outputs": [],
   "source": [
    "create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "id": "7cb31a6c",
   "metadata": {},
   "outputs": [],
   "source": [
    "drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
