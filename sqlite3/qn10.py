# 10. Write a Python program to update all the values of a specific column of a given SQLite table.
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

    cursor.execute(
        "UPDATE people SET name='Tyrion The Imp', age = 35, email='tyrion@branthebroken@got.com' WHERE rowid = 5;")
    conn.commit()

    cursor.execute("SELECT rowid,* FROM people;")
    results = cursor.fetchall()
    print("\nResults after updation:")
    for row in results:
        print(row)


except sqlite3.Error as error:
    print("Error while connecting to DB ", error)

finally:
    if(conn):
        conn.close()
