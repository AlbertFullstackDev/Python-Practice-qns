# 5. Write a Python program to square the elements of a list using map() function.

numbers = list(range(1, 11))

squares = map(lambda number: number * number, numbers)

for number in squares:
    print(number)
