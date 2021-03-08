# 2. Write a Python program to create a function that takes one argument,
#  and that argument will be multiplied with an unknown given number.
# Sample Output:
# Double the number of 15 = 30
# Triple the number of 15 = 45
# Quadruple the number of 15 = 60
# Quintuple the number 15 = 75

def compute(multiplier):
    return lambda number: number * multiplier


result = compute(2)
print('Double the number of 15 =', result(15))

result = compute(3)
print('Triple the number of 15 =', result(15))
