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
def query_read(connection,query):
    cursor=connection.cursor()
    try:
        cursor.execute(query)
        result=cursor.fetchall()
        column_names=[description[0] for description in cursor.description]
        return column_names,result
    except Error as e:
        print(f"Error {e} occured!")

connection=create_connection("Database\\deckcommander_db.sql")

query_create_table="""
CREATE TABLE IF NOT EXISTS players (
id INTEGER PRIMARY KEY AUTOINCREMENT,
username TEXT NOT NULL,
score INT,
highscore INT
);
"""

query_insert_players="""
INSERT INTO players (username,score)
values
('AARON','4300'),
('GIANNIS','3500'),
('SOFIA','2100')
"""

query_read_players="""
SELECT * from players;
"""

#query_execution(connection,query_create_table)

query_execution(connection,query_insert_players)
#cname,c=query_read(connection,query_read_players)
#print(cname,c)