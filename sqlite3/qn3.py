# 3. Write a Python program to connect a database and create a SQLite table within the database.

import sqlite3

try:
    conn = sqlite3.connect('sqlite3/sample2.db')

    cursor = conn.cursor()

    cursor.execute("CREATE TABLE people(name text, age number, email text)")

    conn.commit()

    print("Table created successfully !!!")

except sqlite3.Error as error:
    print("Error: ", error)

finally:
    if(conn):
        conn.close()
