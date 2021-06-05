# 5. Write a Python program to read a given CSV files with initial spaces after a delimiter
#    and remove those initial spaces.

import csv

with open("csv/destinations3.csv", "r", newline="") as csv_file:
    reader = csv.reader(csv_file, skipinitialspace=True)

    for line in reader:
        print(','.join(line))
