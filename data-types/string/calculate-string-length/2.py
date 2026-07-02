"""
Write a Python program to calculate the length of a string recursively without using the built-in len() function.
"""


def recursive_len(s: str) -> int:
    if s == "":
        return 0

    return 1 + recursive_len(s[1:])


user_input = input("Enter a string and get its length: ")
length = recursive_len(user_input)
print(f"Your string has the length: {length}")
