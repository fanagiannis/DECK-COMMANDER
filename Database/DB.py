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
INSERT INTO players (username,score,highscore)
values
('NICK','4000','4000'),
('MPG','3000','3400'),
('AFSASFA','200','2000')
"""

query_read_players="""
SELECT * from players;
"""

#query_execution(connection,query_create_table)

#query_execution(connection,query_insert_users)
cname,c=query_read(connection,query_read_players)
print(cname,c)