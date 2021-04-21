# 7. Write a Python program to remove duplicates from a list.

numbers = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]


new_list = []

[new_list.append(number) for number in numbers if number not in new_list]

print(new_list)
