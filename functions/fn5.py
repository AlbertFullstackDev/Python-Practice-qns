# 5. Write a Python function to calculate the factorial of a number (a non-negative integer).
#  The function accepts the number as an argument.
import math


def number_factorial(number):
    if number == 0:
        return 1
    else:
        return (number * number_factorial(number - 1))


number = int(input("Put a positive integer: "))

number = abs(number)

print(f'Factorial of {number} is: {number_factorial(number)}')
