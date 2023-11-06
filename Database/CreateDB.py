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

connection=create_connection("deckcommander_db.sql")

