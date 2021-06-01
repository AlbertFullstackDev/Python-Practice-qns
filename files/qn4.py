# 4. Write a Python program to read last n lines of a file.
from pathlib import Path


file_path = Path(r"files\demos\sample.txt")

with open(file_path, "r") as file:
    try:
       lines = file.readlines()
       last_lines = lines[-2:]
       for l in last_lines:
           print(l, end="") 
    except Exception as e:
        print(e)
   