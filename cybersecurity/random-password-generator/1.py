"""
Write a Python program that defines a function to generate random passwords of a specified length.
The function takes an optional parameter length, which is set to 8 by default.
If no length is specified by the user, the password will have 8 characters.
"""

import secrets
from string import digits, ascii_letters, punctuation

invalid_chars = {'"', "\\", "/", "'"}
valid_chars = set(digits + ascii_letters + punctuation) - invalid_chars
valid = "".join(valid_chars)


def generate_password(length: int = 8) -> str:
    """
    Generates a random password and returns it as a str.
    """
    password = "".join(secrets.choice(valid) for _ in range(length))
    return password


user_input = input("Please enter the length of the password to be generated: ")
if user_input.isdigit():
    password = generate_password(int(user_input))
else:
    password = generate_password()

print(f"Your generated password is: {password}")
