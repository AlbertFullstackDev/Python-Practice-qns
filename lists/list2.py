# 2. Write a Python program to multiply all the items in a list.

def multiples(numbers):
    total = 1
    for number in numbers:
        total *= number

    return total


numbers = list(range(1, 11))
print(f'The total product is: {multiples(numbers)}')
