# 10. Write a Python program to check whether an element exists within a tuple.

numbers = tuple(range(11))

number = int(input("Enter a number: "))

if number in numbers:
    print(f"{number} exists in a tuple")
else:
    print(f"{number} doesn't exists in a tuple")
