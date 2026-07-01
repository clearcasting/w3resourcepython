"""
Write a Python function that reads a password from a file, computes its SHA-256 hash, and writes the hash to another file.
"""

import hashlib

with open("clear.txt", "r") as file:
    password = file.readline().strip()

encoded_pass = password.encode("utf-8")
hashed_pass = hashlib.sha256(encoded_pass).hexdigest()

with open("hashed.txt", "w") as result_file:
    result_file.write(hashed_pass)
