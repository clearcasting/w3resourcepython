"""
Write a Python program to determine the length of a string by converting it to a list and summing 1 for each element.
"""

user_input = input("Enter a string and get its length: ")
count = sum(1 for _ in list(user_input))

print(f"Your string length is: {count}")
