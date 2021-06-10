# 2. Write a Python program to convert Python object to JSON data.
import json
fruits_color = {"Fruit": ["Mango", "Banana"], "Color": ["Blue", "Red"]}

# Convert py dict to json data(file)
with open('json/fruits.json', 'w') as file:
    json.dump(fruits_color, file, indent=2, sort_keys=True)
