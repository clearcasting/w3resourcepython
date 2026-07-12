"""
Write a Python program that calculates the area of a circle based on the radius entered by the user.
Sample Output :
r = 1.1
Area = 3.8013271108436504
"""

import math


def area_of_circle(radius: float) -> float:
    return math.pi * radius**2


try:
    user_input = float(input("Enter the radius: "))
    area = area_of_circle(user_input)
    print(f"Area = {area}")
except ValueError:
    print("Please enter a valid numeric value for the radius.")
