# 4. Write a Python program to convert Python dictionary object (sort by key) to JSON data.
#     Print the object members with indent level 4.

import json

capitals = {"USA": "Washington DC", "France": "Paris",
            "Japan": "Tokyo", "India": "New Delhi"}

capitals_json = json.dumps(capitals, indent=4, sort_keys=True)

print(capitals_json)
