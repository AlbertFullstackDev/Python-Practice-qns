# 4. Write a Python program to read a given CSV file as a dictionary. 
import csv

with open("transaction.csv","r") as file:
    data = csv.DictReader(file)
    for row in data:
        print(row)