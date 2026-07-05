"""
Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.
Sample String : 'abc', 'xyz'
Expected Result : 'xyc abz'
"""


def swap_chars():
    first_str = input("Enter the first string: ").strip()
    second_str = input("Enter the second string: ").strip()
    if not first_str or not second_str:
        print("Strings cannot be empty.")
        return ""

    new_first = second_str[:2] + first_str[2:]
    new_second = first_str[:2] + second_str[2:]

    return f"{new_first} {new_second}"


print(swap_chars())
