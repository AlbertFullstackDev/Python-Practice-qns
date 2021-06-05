# 1. Write a Python program to read each row from a given csv file and print a list of strings. 
import csv

with open("csv/destinations.csv", "r") as file:
    data = csv.reader(file)
    for line in data:
        stri = " ".join(line)
        print(stri)