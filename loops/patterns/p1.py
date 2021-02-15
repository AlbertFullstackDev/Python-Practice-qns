
#  Write a Python program to construct the following pattern, using a nested for loop.

# *
# * *
# * * *
# * * * *
# * * * * *
num = int(input("Please enter the number of rows: "))
for i in range(1, num+1):  # to print rows
    for j in range(1, i+1):  # to print coluns
        print("*", end=" ")  # print asterisk in column and space infront of it
    print()  # print space ()
