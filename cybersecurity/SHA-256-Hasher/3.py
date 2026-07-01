"""
Write a Python program to compare the SHA-256 hashes of two user-input passwords and print a message indicating whether they match.
"""

import hashlib


def sha256_hasher(password: str) -> str:
    encoded_pass = password.encode("utf-8")
    return hashlib.sha256(encoded_pass).hexdigest()


print("[*] - Note: Both passwords MUST match.")
first_pass = sha256_hasher(input("[*] - Enter your new password: "))
second_pass = sha256_hasher(input("[*] - Enter the password again: "))

if first_pass == second_pass:
    print("[*] - Password successfully changed.")
else:
    print("[*] - ERROR: Both passwords MUST match.")
