"""
Write a Python program to count the number of characters (character frequency) in a string.
Sample String : google.com'
Expected Result : {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}
"""

str1 = "google.com"
chars_count = {}

for char in str1:
    chars_count[char] = chars_count.get(char, 0) + 1

print(chars_count)
