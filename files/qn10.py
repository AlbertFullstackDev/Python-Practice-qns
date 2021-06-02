# 10. Write a Python program to count the frequency of words in a file.


from pathlib import Path

file_path = Path(r"files\demos\sample.txt")

with open(file_path , "r") as file:
    lines =  file.readlines()
    
    words = []

    for line in lines:
        for word in line.split():
             words.append(word)
    
    frequency = len(words)
    print(frequency)