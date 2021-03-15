# 2. Write a Python program to add three given lists using Python map and lambda.

list1 = list(range(1, 6))
list2 = list(range(6, 11))
list3 = list(range(11, 16))
print("Original list: ")
print(list1)
print(list2)
print(list3)

result = map(lambda x, y, z: x + y + z, list1, list2, list3)

print("\nNew list after adding above three lists:")
print(list(result))
