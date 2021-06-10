# 5. Write a Python program to convert JSON encoded data into Python objects.
import json

json_string = '''
 {
  "people": [
    {
      "name": "Albert Sigsbert",
      "age": 22,
      "married": false,
      "languages": [
        "Swahili",
        "English",
        "Korean"
      ],
      "phone": "123-555-7789"
    },
    {
      "name": "Messi",
      "age": 32,
      "married": true,
      "languages": [
        "Spanish",
        "English",
        "Portguese"
      ],
      "phone": null
    }
  ]
}

'''

data = json.loads(json_string)

for person in data['people']:
    print(type(person))
    print(person)

    print(type(person['languages']))
    print(person['languages'])
