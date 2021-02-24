# 6. Write a Python function to check whether a number is in a given range.

def check_range(number):
    if number in range(min_number, max_number + 1):
        print(f"{number} is in the range {min_number}-{max_number}")
    else:
        print("The number is outside the given range.")


number = int(input("Insert a number to checkif its in a given range: "))
max_number = int(input("Insert a maximum number of range: "))
min_number = int(input("Insert a minimum number of range: "))

print(check_range(number))
