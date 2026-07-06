"""
Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing', add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged.
Sample String : 'abc'
Expected Result : 'abcing'
Sample String : 'string'
Expected Result : 'stringly'
"""


def ing_or_ly() -> str:
    user_input = input("Enter a string: ").strip()
    if not user_input or len(user_input) < 3:
        print("String must be at least 3 characters.")
        return user_input

    if user_input.endswith("ing"):
        return user_input + "ly"

    return user_input + "ing"


print(ing_or_ly())
