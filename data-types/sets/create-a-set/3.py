"""
Write a Python program to create a set from user input where the input is a comma-separated string of values.
"""

user_input = input("Enter comma separated values: ")

result = set(user_input.split(","))
print(result)
