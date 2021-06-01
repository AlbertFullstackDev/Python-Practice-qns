# 2. Write a Python program to read first n lines of a file.

from pathlib import Path
from itertools import islice
path = Path("C:\\Users\\AM\\Desktop\\DEMO\\file.txt")

with open(path) as file:
  for line in islice(file,2):
    print(line)
