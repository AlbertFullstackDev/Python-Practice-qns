# 7. Write a Python program to insert values to a table from user input.

import sqlite3
name = input('Name: ')
age = input('Age: ')
email = input('Email: ')


try:
    conn = sqlite3.connect('sqlite3/sample2.db')

    cursor = conn.cursor()

    cursor.execute("INSERT INTO people VALUES(?,?,?);", (name, age, email))

    conn.commit()

    print("Data inserted succesfully....")


except sqlite3.Error as error:
    print("Error while connecting to DB ", error)

finally:
    if(conn):
        conn.close()
