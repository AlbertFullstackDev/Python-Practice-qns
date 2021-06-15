import sqlite3

conn = sqlite3.connect('sqlite3/movie.db')

cursor = conn.cursor()

# cursor.execute("""CREATE TABLE movies (
#     title text,
#     vote_average REAL,
#     release_date text
#    )
# """)

# movies = [
#     ('Cruella', 8.6, '2021-05-26'),
#     ('The Conjuring: The Devil Made Me Do It', 8.2, '2021-05-25'),
#     ('"Wrath of Man', 7.9, '2021-04-22')
# ]
# cursor.executemany("INSERT INTO movies VALUES(?,?,?)", movies)

# fetch All movies
cursor.execute("SELECT * FROM movies")
movie_list = cursor.fetchall()
print(movie_list)

# Commit executions
conn.commit()

# Close connection
conn.close()
