# 6. Write a Python program to create a new JSON file from an existing JSON file.

import json

with open('json/books.json') as file:
    data = json.load(file)

    with open('json/new_books.json', 'w') as new_file:
        json.dump(data, new_file, indent=3, sort_keys=True)
