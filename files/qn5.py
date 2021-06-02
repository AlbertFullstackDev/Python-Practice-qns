# 5. Write a Python program to read a file line by line and store it into a list.
from pathlib import Path

file_path = Path() / "files/demos/sample.txt"

with open(file_path , "r") as file:
    lines = [line for line in file.readlines()] 
    print(lines)

