# 8. Write a Python program to count the number of rows of a given SQLite table.
import sqlite3


try:
    conn = sqlite3.connect('sqlite3/sample2.db')

    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(rowid) FROM people;")

    results = cursor.fetchall()

    print("Number of rows:", results[0][0])


except sqlite3.Error as error:
    print("Error while connecting to DB ", error)

finally:
    if(conn):
        conn.close()
