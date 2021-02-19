# 2. Write a Python function to sum all the numbers in a list.
# Sample List : (8, 2, 3, 0, 7)
# Expected Output : 20


def sum_of_numbers(numbers):
    sum = 0
    for number in numbers:
        sum += number
    return sum


#numbers = list(range(1, 11))

numbers = [8, 2, 3, 0, 7]

print(f'Sum: {sum_of_numbers(numbers)}')
