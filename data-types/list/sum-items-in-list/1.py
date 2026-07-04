"""
Write a Python program to sum all the items in a list.
"""


def sum_list(data: list) -> int:
    result = 0

    for item in data:
        result += item

    return result


data = [1, 2, 3, 4]
print(sum_list(data))

# quick way
print(sum(data))
