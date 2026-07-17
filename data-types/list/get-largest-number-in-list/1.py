"""
Write a Python program to get the largest number from a list.
"""


def largest(nums: list[int]) -> int:
    if not nums:
        return None

    result = nums[0]
    for num in nums:
        if num > result:
            result = num

    return result


numbers = [1, 0, 99, 5]
print(largest(numbers))

# max() function
print(max(numbers))
