#  Write a Python program to construct the following pattern(pyramid), using a nested for loop.

#      *
#    *   *
#   *  *  *
#  *  *  *  *
# *  *  *  *  *

row = int(input("Enter number of rows: "))
for i in range(0, row):
    for j in range(0, row-i-1):  # loop to print spaces before asterisks
        print(end=" ")
    for j in range(0, i+1):  # loop to print *
        print("*", end=" ")
    print()
