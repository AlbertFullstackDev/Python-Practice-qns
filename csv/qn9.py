# 9. Write a Python program to create an object for writing and iterate over the rows to print the values.
# importing the csv module
import csv

# my data rows as dictionary objects
mydict = [{'branch': 'EIM', 'gpa': '4.0', 'name': 'Neema', 'year': '2'},
          {'branch': 'BRM', 'gpa': '3.5', 'name': 'Salma', 'year': '2'},
          {'branch': 'IT', 'gpa': '3.3', 'name': 'Antony', 'year': '2'},
          {'branch': 'INF', 'gpa': '4.5', 'name': 'Japhet', 'year': '1'},
          {'branch': 'CS', 'gpa': '4.8', 'name': 'Kelvin', 'year': '3'},
          {'branch': 'BRD', 'gpa': '3.1', 'name': 'Joseph', 'year': '2'}]

# field names
fields = ['name', 'branch', 'year', 'gpa']

# writing to csv file
with open("csv/university_records.csv", 'w', newline="") as csvfile:
    # creating a csv dict writer object
    writer = csv.DictWriter(csvfile, fieldnames=fields,)

    # writing headers (field names)
    writer.writeheader()

    # writing data rows
    writer.writerows(mydict)
