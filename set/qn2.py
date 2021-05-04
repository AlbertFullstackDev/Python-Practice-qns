# Write a Python program to iterate over sets.

numbers = [1, 2, 6, 6, 7, 8, 2, 1, 9, 8, 3, 6, 4, 5]

no_duplicates = {number for number in numbers}

for number in no_duplicates:
    print(number)
