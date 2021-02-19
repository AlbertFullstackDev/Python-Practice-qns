# 3. Write a Python function to multiply all the numbers in a list.
# Sample List : (8, 2, 3, -1, 7)
# Expected Output : -336


def multiply(numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


# numbers = list(range(1, 10))
numbers = (8, 2, 3, -1, 7)

print(f'Total:{multiply(numbers)}')
