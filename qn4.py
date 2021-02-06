
# Write a Python program which accepts the radius of a circle from the user and compute the area.
# Sample Output :
# r = 1.1
# Area = 3.8013271108436504
import math
radius_of_circle = float(input("Radius of Circle: "))
area_of_circle = math.pi * (radius_of_circle ** 2)
print(f'r = {radius_of_circle}')
print(F'Area = {area_of_circle}')
