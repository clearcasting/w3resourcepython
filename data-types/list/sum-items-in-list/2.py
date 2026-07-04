"""
Write a Python program to find the sum of only the positive numbers in a given list.
"""


def sum_positives(data: list[int]) -> int:
    sum = 0

    for item in data:
        if item > 0:
            sum += item

    return sum


data = [1, -1, 2, 3, 4, -10]
print(sum_positives(data))

# One-liner
print(sum(item for item in data if item > 0))
