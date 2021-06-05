# 2. Write a Python program to read a given CSV file having tab delimiter.
import csv
data_list = [
    ['department_id', 'department_name', 'manager_id', 'location_id'],
    [10, 'Administration', 200, 1700],
    [20, 'Marketing', 201, 1800],
    [30, 'IT', 202, 1900],
    [40, 'Sales', 203, 2000],
    [50, 'Finance', 204, 2100],
    [60, 'Benefit', 205, 2200],
    [70, 'Treasury', 206, 2300],
    [80, 'Deposit', 207, 2400]
]
with open("csv/destinations2.csv", "w", newline="")as csv_file:
    data = csv.writer(csv_file, delimiter="\t")
    data.writerows(data_list)

with open("csv/destinations2.csv", "r") as file:
    csv_reader = csv.reader(file, delimiter="\t")
    for line in csv_reader:
        print(' '.join(line))
