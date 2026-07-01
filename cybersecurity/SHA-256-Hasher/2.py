"""
Write a Python script to prompt the user for a password, hash it using SHA-256, and then print both the original and hashed values.
"""

import hashlib


def sha256_hasher(password: str) -> str:
    encoded_password = password.encode("utf-8")
    return hashlib.sha256(encoded_password).hexdigest()


password = input("Enter your password: ")
hashed_password = sha256_hasher(password)
print(f"Cleartext password: {password}")
print(f"Hashed password: {hashed_password}")
