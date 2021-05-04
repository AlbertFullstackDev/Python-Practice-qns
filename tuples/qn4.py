# 4. Write a Python program to unpack a tuple in several variables.

numbers = tuple(range(11))
first, *others, last = numbers
print(first)
print(others)
print(last)
