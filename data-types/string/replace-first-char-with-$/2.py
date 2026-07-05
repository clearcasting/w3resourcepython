"""
Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.
Sample String : 'restart'
Expected Result : 'resta$t'

Write a Python program to implement this replacement using a for-loop and conditional checks.
"""


def str_replacer() -> str:
    user_input = input("Enter a word: ").strip()
    if not user_input:
        print("String cannot be empty.")
        return ""

    first_char = user_input[0]
    result = []

    for i, char in enumerate(user_input):
        if char == first_char and i != 0:
            result.append("$")
        else:
            result.append(char)

    return "".join(result)


print(str_replacer())
