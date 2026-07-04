"""
Write a Python program to create a function that takes one argument, and that argument will be multiplied with an unknown given number.

Sample Output:
Double the number of 15 = 30
Triple the number of 15 = 45
Quadruple the number of 15 = 60
Quintuple the number 15 = 75
"""


def multiplier(n):
    return lambda a: a * n


# double is now equivalent to: lambda a: a * 2
double = multiplier(2)
triple = multiplier(3)
quadruple = multiplier(4)
quintuple = multiplier(5)

# double is now equivalent to: 15 * 2
print(f"Double the number of 15 = {double(15)}")
print(f"Triple the number of 15 = {triple(15)}")
print(f"Quadruple the number of 15 = {quadruple(15)}")
print(f"Quintuple the number of 15 = {quintuple(15)}")
