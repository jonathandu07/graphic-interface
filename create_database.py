import sqlite3

connection = sqlite3.connect("mydatabase.db")
cur = connection.cursor()
cur.execute(".")