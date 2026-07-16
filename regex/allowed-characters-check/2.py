"""
Write a Python program to validate that a string contains only lowercase letters and digits.
"""

import re


def matcher(pattern: str, input_str: str) -> bool:
    return bool(re.match(pattern, input_str))


str1 = "hello30421"
str2 = "hello!340"
pattern = r"^[a-z0-9]+$"

print(matcher(pattern, str1))
print(matcher(pattern, str2))
