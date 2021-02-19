# 4. Write a Python program to reverse a string.
# Sample String : "1234abcd"
# Expected Output : "dcba4321"

def reverse_string(string):
    for letter in range(len(string)-1, -1, -1):
        print(string[letter], end="")


reverse_string("Hello World")
