# 3. Write a Python program to get the largest number from a list.

def largest(numbers):
    largest = numbers[0]
    for number in numbers:
        if number > largest:
            largest = number

    return largest


numbers = [9, 5, 87, 5, 3, 88, 25, 63, 47, 10, 2, 89, 525, 52, 14, 336]
print(f'The largest number is: {largest(numbers)}')
