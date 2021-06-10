# 1. Write a Python program to convert JSON data to Python object.
import urllib.request
import json
import os

api_key = os.getenv('TMDB_API_KEY')

with urllib.request.urlopen("https://api.themoviedb.org/3/movie/popular?api_key=" + str(api_key) + "&page=1") as response:
    popular_movies = response.read()

    data = json.loads(popular_movies)

    print(json.dumps(data, indent=2))
