"""
Write a Python program to recursively compute the frequency of each character in a string without using loops.
"""

str1 = "google.com"


def recursive(s: str, index: int = 0, counts: dict = None) -> dict:
    if counts is None:
        counts = {}

    if index == len(s):
        return counts

    char = s[index]
    counts[char] = counts.get(char, 0) + 1

    return recursive(s, index + 1, counts)


print(recursive(str1))
