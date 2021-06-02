# 8. Write a python program to find the longest words.

from pathlib import Path

file_path = Path(r"files\demos\sample.txt")

with open(file_path , "r") as file:
    lines =  file.readlines()
    
    words = []

    for line in lines:
        for word in line.split():
             words.append(word)
    
    longest = max(words , key=len)
    print(longest)