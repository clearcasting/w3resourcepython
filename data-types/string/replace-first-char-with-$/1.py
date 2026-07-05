"""
Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.
Sample String : 'restart'
Expected Result : 'resta$t'
"""


def char_replacer() -> str:
    user_input = input("Enter a word: ").strip()
    if not user_input:
        print("String cannot be empty.")
        return ""

    first_char = user_input[0]
    remainder = user_input[1:]

    return first_char + remainder.replace(first_char, "$")


print(char_replacer())
