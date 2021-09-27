{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "d56004b6",
   "metadata": {},
   "outputs": [],
   "source": [
    "import psycopg2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "id": "0bafcccb",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sql_queries import create_table_queries,drop_table_queries"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "6e300028",
   "metadata": {},
   "outputs": [],
   "source": [
    "def create_database():\n",
    "    \"\"\"\n",
    "    - Creates and connects to the sparkifydb\n",
    "    - Returns the connection and cursor to sparkifydb\n",
    "    :return: cursor an connection\n",
    "    \"\"\"\n",
    "    \n",
    "    # connect to default database\n",
    "    conn = psycopg2.connect(\"host=127.0.0.1 dbname=postgres user=postgres password=Learn@123\")\n",
    "    conn.set_session(autocommit=True)\n",
    "    cur = conn.cursor()\n",
    "    \n",
    "    # create sparkify database with UTF8 encoding\n",
    "    cur.execute(\"DROP DATABASE IF EXISTS sparkifydb\")\n",
    "    cur.execute(\"CREATE DATABASE sparkifydb WITH ENCODING 'utf8' TEMPLATE template0\")\n",
    "\n",
    "    # close connection to default database\n",
    "    conn.close()    \n",
    "    \n",
    "    # connect to sparkify database\n",
    "    conn = psycopg2.connect(\"host=127.0.0.1 dbname=sparkifydb user=postgres password=Learn@123\")\n",
    "    cur = conn.cursor()\n",
    "    \n",
    "    return cur, conn"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "3544544a",
   "metadata": {},
   "outputs": [],
   "source": [
    "def drop_tables(cur, conn):\n",
    "    \"\"\"\n",
    "    Drops each table using the queries in `drop_table_queries` list.\n",
    "    \"\"\"\n",
    "    for query in drop_table_queries:\n",
    "        cur.execute(query)\n",
    "        conn.commit()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "d71b8385",
   "metadata": {},
   "outputs": [],
   "source": [
    "def create_tables(cur, conn):\n",
    "    \"\"\"\n",
    "    Creates each table using the queries in `create_table_queries` list. \n",
    "    \"\"\"\n",
    "    for query in create_table_queries:\n",
    "        cur.execute(query)\n",
    "        conn.commit()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "c5d4c0a3",
   "metadata": {},
   "outputs": [],
   "source": [
    "def main():\n",
    "    \"\"\"\n",
    "    - Drops (if exists) and Creates the sparkify database. \n",
    "    \n",
    "    - Establishes connection with the sparkify database and gets\n",
    "    cursor to it.  \n",
    "    \n",
    "    - Drops all the tables.  \n",
    "    \n",
    "    - Creates all tables needed. \n",
    "    \n",
    "    - Finally, closes the connection. \n",
    "    \"\"\"\n",
    "    cur, conn = create_database()\n",
    "    \n",
    "    drop_tables(cur, conn)\n",
    "    create_tables(cur, conn)\n",
    "\n",
    "    conn.close()\n",
    "\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    main()"
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
