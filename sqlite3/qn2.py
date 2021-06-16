# 2. Write a Python program to create a SQLite database connection to a database that resides in the memory.

import sqlite3

try:
    conn = sqlite3.connect(':memory:')

    print("Sqlite memory DB created successfully !!!")

except sqlite3.Error as error:
    print("Error while creating memory DB ", error)

finally:
    if(conn):
        conn.close()
