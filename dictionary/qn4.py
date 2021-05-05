# 4. Write a Python script to check whether a given key already exists in a dictionary.

dictionary = dict(x=1, y=2, z=3)

key = input("Enter key to check if its in dictionary: ")

if key in dictionary:
    print(f"{key} exists in a dictionary as a key")
else:
    print(f"{key} DOESN'T exist in a dictionary as a key")
