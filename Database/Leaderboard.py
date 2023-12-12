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
    score INT,
    round INT
    );
    """
    query_execution(connection,query_create_table)

def insert_leaderboard(query):
    players=query_execution(connection,query)
    
def read_leaderboard(query):
    query_read_players=query
    players=query_read(connection,query_read_players)
    return players

def game_over_add_leaderboard(username,score,round):
    game_over_query="INSERT INTO players(username,score,round) VALUES ('"+ str(username) +"',"+str(score)+","+str(round)+")"
    insert_leaderboard(game_over_query)

connection=create_connection("Database\\deckcommander_db.sql")

#query = "DELETE FROM players WHERE id >= 4"
#query_execution(connection,query)

#query="""
#INSERT INTO players(username,score,round)
#VALUES ('GIORGOS',1500,2),('NIKOS',3300,3),('KENOBI',200,1)
#"""
#query_execution(connection,create_leaderboard())
#insert_leaderboard(query)
#query="""
#SELECT username,score FROM players ORDER BY score DESC;
#"""
#columns,res=read_leaderboard(query)
#print(columns)
#print(players)
#for res in res:
#    print (res[0])

#user=input("Search user : ")
#query="SELECT id FROM players WHERE username = '"+user+"'"
#players,res=read_leaderboard(query)
#for player in players:
#    if res==[]:
#        print("PLAYER NOT FOUND!")
#        pass
#    else:
#        print(res)

   









