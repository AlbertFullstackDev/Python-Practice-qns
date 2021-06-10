# 3. Write a Python program to convert Python objects into JSON strings.
#   Print all the values.

import json
fruits_color = {"Fruit": ["Mango", "Banana"], "Color": ["Blue", "Red"]}

# Convert py dict to json string
fruits_color_json = json.dumps(fruits_color, indent=2)

print(type(fruits_color_json))
print(fruits_color_json)
