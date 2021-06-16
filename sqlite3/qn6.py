# 6. Write a Python program to insert a list of records into a given SQLite table.
import sqlite3
people = [
    ('Arya Stark', 16, 'aryastark@got.com'),
    ('Ramsey Bolton', 26, 'boltonramsey@got.com'),
    ('Lyanna Mormont', 8, 'lyannamormont@got.com'),
    ('Walder Frey', 78, 'walderfrey@got.com')
]

try:
    conn = sqlite3.connect('sqlite3/sample2.db')

    cursor = conn.cursor()

    cursor.executemany("INSERT INTO people VALUES(?,?,?);", people)

    conn.commit()

    print("Data inserted succesfully....")

except sqlite3.Error as error:
    print("Error while connecting to DB ", error)

finally:
    if(conn):
        conn.close()
