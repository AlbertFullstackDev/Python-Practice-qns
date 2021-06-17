# 12. Write a Python program to alter a given SQLite table.

import sqlite3

try:
    conn = sqlite3.connect('sqlite3/sample2.db')

    cursor = conn.cursor()

    cursor.execute("ALTER TABLE people ADD salary text;")

    conn.commit()


except sqlite3.Error as error:
    print("Error while connecting to DB ", error)

finally:
    if(conn):
        conn.close()
