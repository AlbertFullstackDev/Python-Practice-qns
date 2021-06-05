# 8. Write a Python program that reads each row of a given csv file and skip the header of the file.
#    Also print the number of rows and the field names.

import csv

with open("csv/destinations.csv", "r", newline="") as file:
    reader = csv.DictReader(file)

    print(f"No of fieldnames: {len(reader.fieldnames)}")

    rowcount = 0
    for line in reader:
        rowcount += 1
        print(line['department_name'])

    print(f"No of rows: {rowcount}")
