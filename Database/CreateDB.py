import sqlite3
from sqlite3 import Error

def create_connection(path):
    connection=None
    try:
        connection=sqlite3.connect(path)
        print("DB Connected!")
    except Error as e:
        print(f"Error '{e}' occured!")
    return connection

def query_execution(connection,query):
    cursor=connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Executed!")
    except Error as e:
        print(f"Error '{e}' occured!")
        pass

connection=create_connection("deckcommander_db.sql")

query_create_table="""
CREATE TABLE IF NOT EXISTS players (
id INTEGER PRIMARY KEY AUTOINCREMENT,
username TEXT NOT NULL,
score INTEGER,
highscore INTEGER 
);
"""

query_execution(connection,query_create_table)
