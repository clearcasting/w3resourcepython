"""
Write a Python program to create a lambda function that takes two numbers and returns their sum if their product is even, otherwise returns their difference.
"""

sum_even = lambda a, b: a + b if (a * b) % 2 == 0 else a - b
print(sum_even(4, 3))
print(sum_even(5, 3))
