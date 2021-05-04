# Write a Python program to remove an item from a set if it is present in the set.

numbers = set(range(10))
if 8 in numbers:
    numbers.remove(8)
else:
    pass
print(numbers)
