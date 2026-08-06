"""
Write a Python function that takes a list of words and return the longest word and the length of the longest one.
Sample Output:
Longest word: Exercises
Length of the longest word: 9
"""


def get_longest_word(words: list[str]) -> tuple[str, int]:
    if not words:
        return "", 0

    longest = max(words, key=len)

    return longest, len(longest)


words = ["Exercises", "Test", "Hello", "World", "Longing"]

word, length = get_longest_word(words)

print(f"Longest word: {word}")
print(f"Length of the longest word: {length}")
