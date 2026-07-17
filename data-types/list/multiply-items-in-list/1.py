"""
Write a Python program to multiply all the items in a list.
"""


def multiply_items(nums: list[int]) -> int:
    if not nums:
        return 0

    result = 1
    for num in nums:
        result *= num

    return result


# Should return 18
numbers = [3, 1, 2, 3]

print(multiply_items(numbers))
