# 1. Write a Python program to triple all numbers of a given list of integers. Use Python map

numbers = list(range(1, 11))
triple = list(map(lambda number: number * 3, numbers))
print(f"""
Original: {numbers} 
Triple: {triple}""")
