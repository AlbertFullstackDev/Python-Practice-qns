# 11. Write a Python program to write a Python dictionary to a csv file.
#     After writing the CSV file read the CSV file and display the content.

import csv

# my data rows as dictionary objects
mydict = [{'branch': 'EIM', 'gpa': '4.0', 'name': 'Neema', 'year': '2'},
          {'branch': 'BRM', 'gpa': '3.5', 'name': 'Salma', 'year': '2'},
          {'branch': 'IT', 'gpa': '3.3', 'name': 'Antony', 'year': '2'},
          {'branch': 'INF', 'gpa': '4.5', 'name': 'Japhet', 'year': '1'},
          {'branch': 'CS', 'gpa': '4.8', 'name': 'Kelvin', 'year': '3'},
          {'branch': 'BRD', 'gpa': '3.1', 'name': 'Joseph', 'year': '2'}]

with open("csv/university_records.csv", "w", newline="") as file:
    fields = ['branch', 'gpa', 'name', 'year']
    csv_writer = csv.DictWriter(file, fieldnames=fields)

    csv_writer.writerows(mydict)

with open("csv/university_records.csv", "r", newline="") as file:
    csv_reader = csv.DictReader(file)

    for line in csv_reader:
        print(line)
