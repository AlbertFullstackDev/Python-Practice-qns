# 11. Write a Python program to delete a specific row from a given SQLite table.
import sqlite3

try:
    conn = sqlite3.connect('sqlite3/sample2.db')

    cursor = conn.cursor()

    cursor.execute("INSERT INTO people VALUES(?,?,?)",
                   ('Daenarys Taegeryan', 29, 'Daenarys@got.com'))

    conn.commit()

    cursor.execute("SELECT rowid,* FROM people;")
    results = cursor.fetchall()
    print("Results after insertion:\n",)
    for row in results:
        print(row)

    cursor.execute("DELETE FROM people WHERE rowid=6;")

    conn.commit()

    cursor.execute("SELECT rowid,* FROM people;")
    results = cursor.fetchall()
    print("Results after deletion:\n",)
    for row in results:
        print(row)


except sqlite3.Error as error:
    print("Error while connecting to DB ", error)

finally:
    if(conn):
        conn.close()
