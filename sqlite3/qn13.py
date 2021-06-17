# 13. Write a Python program to create a backup of a SQLite database.
import sqlite3
try:
    conn = sqlite3.connect('sqlite3/sample2.db')
    b_conn = sqlite3.connect('sqlite3/backup.db')

    conn.backup(b_conn)
    b_conn.close()

except sqlite3.Error as error:
    print("Error while connecting to DB ", error)

finally:
    if conn and b_conn:
        conn.close()
        b_conn.close()
