# 1. Write a Python program to create a SQLite database and
#   connect with the database and print the version of the SQLite database.

import sqlite3

try:
    conn = sqlite3.connect('sqlite3/sample.db')

    cursor = conn.cursor()

    cursor.execute("select sqlite_version()")

    record = cursor.fetchall()

    print("Sqlite DB version is ", record[0][0])

except sqlite3.Error as error:
    print("Error while connecting to DB ", error)

finally:
    if(conn):
        conn.close()
