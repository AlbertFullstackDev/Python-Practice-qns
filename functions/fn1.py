# 1. Write a Python function to find the Max of three numbers.
def maximum_number(first_number, second_number, third_number):
    if second_number < first_number > third_number:
        maximum_number = first_number
    elif first_number < second_number > third_number:
        maximum_number = second_number
    else:
        maximum_number = third_number

    return maximum_number


print(f'Max number: {maximum_number(9,2,3)}')

# def max_of_two(x, y):
#     if x > y:
#         return x
#     return y


# def max_of_three(x, y, z):
#     return max_of_two(x, max_of_two(y, z))


# print(max_of_three(3, 6, -5))
