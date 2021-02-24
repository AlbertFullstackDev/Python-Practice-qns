# 10. Write a Python program to print the even numbers from a given list.
# Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Expected Result : [2, 4, 6, 8]

def even_number_list(sample_list):
    even_numbers = []

    for number in sample_list:
        if number % 2 == 0:
            even_numbers.append(number)
    return even_numbers


print(even_number_list([1, 2, 3, 4, 5, 6, 7, 8, 9]))
