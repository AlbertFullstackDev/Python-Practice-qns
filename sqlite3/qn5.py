# 5. Write a Python program to create a table and insert some records in that table.
#  Finally selects all rows from the table and display the records.

import sqlite3
people = [
    ('John Doe', 22, 'johndoe@gmail.com'),
    ('Jane Doe', 19, 'janedoe@gmail.com'),
    ('John Snow', 35, 'johnsnow@gmail.com'),
    ('Ygritte Snow', 28, 'johnsnow@gmail.com'),
    ('Samuell Tarly', 29, 'samtarly@gmail.com')
]

try:
    conn = sqlite3.connect('sqlite3/sample2.db')

    cursor = conn.cursor()

    cursor.executemany("INSERT INTO people VALUES(?,?,?);", people)

    cursor.execute("SELECT * FROM people")

    record = cursor.fetchall()

    for person in record:
        print(person)

except sqlite3.Error as error:
    print("Error while connecting to DB ", error)

finally:
    if(conn):
        conn.close()
