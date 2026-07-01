"""
Write a Python program that defines a function and takes a password string as input and returns its SHA-256 hashed representation as a hexadecimal string.
"""

import hashlib


def sha256_hasher(password: str) -> str:
    """
    Returns the hexadecimal string of the sha256 encoded password.
    """
    encoded_password = password.encode("utf-8")
    return hashlib.sha256(encoded_password).hexdigest()


password = input("Enter your password: ")
hashed_password = sha256_hasher(password)
print(f"Your SHA-256 hashed password is: {hashed_password}")
