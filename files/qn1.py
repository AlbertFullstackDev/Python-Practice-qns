# 1. Write a Python program to read an entire text file.
from pathlib import Path

path = Path("C:\\Users\\AM\\Desktop\\DEMO\\file.txt")

print(path.read_text())