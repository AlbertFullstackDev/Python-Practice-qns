# 1. Write a Python program to sum all the items in a list.

numbers = list(range(1, 11))

sum = 0
for number in numbers:
    sum += number


print(f'sum is: {sum}')
