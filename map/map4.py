# 4. Write a Python program to create a list containing the power of said number
#    in bases raised to the corresponding number in the index using Python map.

base_numbers = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
powers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = list(map(pow, base_numbers, powers))

print(result)
