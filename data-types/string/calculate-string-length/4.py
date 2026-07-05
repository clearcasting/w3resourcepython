"""
Write a Python program to use list comprehension and the sum() function to calculate the total number of characters in a string.
"""

s = "hello, world!"
chars = sum(1 for _ in s)
print(chars)
