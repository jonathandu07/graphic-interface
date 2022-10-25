import sqlite3

conn = sqlite3.connect('mydatabase.db')

#create cursor ( pointeur)

cur = conn.cursor()

# request to create a table students

req  = "CREATE TABLE students ( id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, email TEXT NOT NULL, age INTEGER NOT NULL"

# execute request

cur.execute(req)

# Send request

conn.commit()

conn.close()