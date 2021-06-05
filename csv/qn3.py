# 3. Write a Python program to read a given CSV file as a list.

import csv

with open("transaction1.csv","r")as file:
    data = csv.reader(file )
    print(list(file))