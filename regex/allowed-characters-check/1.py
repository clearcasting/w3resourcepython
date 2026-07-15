"""
Write a Python program to check that a string contains only a certain set of characters (in this case a-z, A-Z and 0-9).
"""

import re


def matcher(pattern: str, input_str: str) -> bool:
    return bool(re.match(pattern, input_str))


str1 = "Hello30421"
str2 = "Hello!340"
pattern = r"^[a-zA-Z0-9]+$"

print(matcher(pattern, str1))
print(matcher(pattern, str2))
