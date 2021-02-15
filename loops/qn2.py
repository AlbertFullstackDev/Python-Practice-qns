# Write a Python program to convert temperatures to and from celsius, fahrenheit.
# [ Formula : c/5 = f-32/9 [ where c = temperature in celsius and f = temperature in fahrenheit ]
# Expected Output :
# 60°C is 140 in Fahrenheit
# 45°F is 7 in Celsius


user_input = int(input('''
    
 Program to convert temperatures to and from celsius, fahrenheit
           ----Menu---
           
    1.Press 1 to enter celsius
    2.Press 2 to enter fahrenheit
    3.Press 3 to convert both fahreinheit and celsius
'''))

if user_input == 1:
    c = float(input("Temp(°C):"))
    f = (((c) * (9 / 5)) + 32)
    print(f"{c}°C is {f} in Fahreinheit")
elif user_input == 2:
    f = float(input("Temp(°F):"))
    c = (f - 32) * (5 / 9)
    print(f"{f}°F is {c} in Celsius")
elif user_input == 3:
    celsius = float(input("Temp(°C):"))
    f = (((celsius) * (9 / 5)) + 32)
    fahrenheit = float(input("Temp(°F):"))
    c = (fahrenheit - 32) * (5 / 9)
    print(f"{celsius}°C is {f} in fahrenheit")
    print(f"{fahrenheit}°F and {c} in celsius")
else:
    print("Please select between 1 and 3")
