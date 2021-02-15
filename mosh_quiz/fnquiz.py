# Fizz Buzz Problem
# Create a fn called fizz_buzz() which takes an input of an integer
# If the input is divisible by 3 it will return the string 'Fizz'
# If the input is divisible by 5 it will return the string 'Buzz'
# If the input is divisible by both 3 and 5 it will return the string 'FizzBuzz' eg:15
# If the input is any other number it will return the number itself 'FizzBuzz' eg:7

def fizz_buzz(number):
    if (number % 3 == 0) and (number % 5 == 0):
        return 'FizzBuzz'
    elif number % 3 == 0:
        return 'Fizz'
    elif number % 5 == 0:
        return 'Buzz'
    else:
        return number


print(fizz_buzz(7))
