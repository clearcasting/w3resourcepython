"""
Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
Sample value of n is 5
Expected Result : 615
"""


def number_expansion(n: int) -> int:
    n_str = str(n)
    return n + int(n_str * 2) + int(n_str * 3)


print(number_expansion(5))
