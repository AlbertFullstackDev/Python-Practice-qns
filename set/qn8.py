# Write a Python program to create set difference.

first = set(range(10))
second = set(range(5, 15))

difference = first - second
difference2 = second - first

print(f'difference1 = {difference} and difference2 = {difference2}')
