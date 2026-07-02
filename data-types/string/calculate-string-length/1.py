"""
Write a Python program to calculate the length of a string.
(Do not use len())
"""

user_input = input("Enter a string: ")

length = 0
for _ in user_input:
    length += 1

print(f"The string length is: {length}")
