# 9. Write a Python program to count the number of lines in a text file

from pathlib import Path

file_path = Path() / "files/demos/sample.txt"

with open(file_path , "r") as file:
    print(len(file.readlines()))