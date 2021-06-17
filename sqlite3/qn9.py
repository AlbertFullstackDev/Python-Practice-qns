# 9. Write a Python program to update a specific column value of a given table
#    and select all rows before and after updating the said table.

import sqlite3

try:
    conn = sqlite3.connect('sqlite3/sample2.db')

    cursor = conn.cursor()

    cursor.execute("SELECT rowid,* FROM people;")

    results = cursor.fetchall()
    print("Results before updation:\n",)
    for row in results:
        print(row)

    cursor.execute("UPDATE people SET age = 18 WHERE rowid = 1;")
    conn.commit()

    cursor.execute("SELECT rowid,* FROM people;")
    results = cursor.fetchall()
    print("Results after updation:\n",)
    for row in results:
        print(row)


except sqlite3.Error as error:
    print("Error while connecting to DB ", error)

finally:
    if(conn):
        conn.close()
