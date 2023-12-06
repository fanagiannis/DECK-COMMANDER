import pygame
import pygame_menu
import sqlite3

from sqlite3 import Error

def create_connection(path):
    connection=None
    try:
        connection=sqlite3.connect(path)
        print("Connected to Database! ")
    except Error as e:
        print(f"Error '{e}' occured!")
    return connection

def query_execution(connection,query):
    cursor=connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Executed query!")
    except Error as e:
        print(f"Error '{e}' occured!")
        pass
def query_read(connection,query):
    cursor=connection.cursor()
    try:
        cursor.execute(query)
        result=cursor.fetchall()
        column_names=[description[0] for description in cursor.description]
        return column_names,result
    except Error as e:
        print(f"Error {e} occured!")

def create_leaderboard():
    query_create_table="""
    CREATE TABLE IF NOT EXISTS players (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    score INT
    );
    """
    query_execution(connection,query_create_table)

def insert_leaderboard(query):
    query_insert_players=query
    players=query_execution(connection,query_insert_players)
    

def read_leaderboard(query):
    query_read_players=query
    players=query_read(connection,query_read_players)
    for player in players:
        print(player)

connection=create_connection("Database\\deckcommander_db.sql")

#create_leaderboard()
#insert_leaderboard()
#query="""
#SELECT id FROM players WHERE username='GIANNIS'
#"""
#read_leaderboard(query)
user=input("Search user : ")
query="SELECT id FROM players WHERE username = '"+user+"'"
read_leaderboard(query)







