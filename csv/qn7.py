# 7. Write a Python program to read specific columns of a given CSV file and print the content of the columns.
import csv

with open("csv/destinations.csv", "r", newline="") as file:
    reader = csv.DictReader(file)

    print(reader.fieldnames[1], end="\n\n")
    for line in reader:
        print(line['department_name'])
