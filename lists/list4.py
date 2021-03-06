# 4. Write a Python program to get the smallest number from a list.

def smallest(numbers):
    smallest = numbers[0]
    for number in numbers:
        if number < smallest:
            smallest = number

    return smallest


numbers = [9, 5, 87, 5, 3, 88, 25, 63, 47, 10, 2, 89, 525, 52, 14, 336]
print(f'The smallest number is: {smallest(numbers)}')
