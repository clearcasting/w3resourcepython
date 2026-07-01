"""
Write a Python program that defines a function and takes a password string as input and returns its SHA-256 hashed representation as a hexadecimal string.
"""

import hashlib


def sha256_hasher(password: bytes) -> str:
    """
    Returns the hexadecimal string of the sha256 encoded password.
    """
    return hashlib.sha256(password).digest().hex()


print(sha256_hasher(b"password"))
