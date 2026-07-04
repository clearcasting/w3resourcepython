"""
Write a Python program to count character occurrences case-insensitively in a string and output the frequency table.
"""

str1 = "GoOglE.com"
char_counts = {}

for char in str1:
    char = char.lower()
    char_counts[char] = char_counts.get(char, 0) + 1

print(char_counts)
