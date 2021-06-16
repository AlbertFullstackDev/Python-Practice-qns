# 4. Write a Python program to list the tables of given SQLite database file.

import sqlite3

try:
    conn = sqlite3.connect('sqlite3/sample2.db')

    cursor = conn.cursor()

    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")

    table_names = cursor.fetchall()

    print(table_names)

except sqlite3.Error as error:
    print("Error: ", error)

finally:
    if(conn):
        conn.close()
