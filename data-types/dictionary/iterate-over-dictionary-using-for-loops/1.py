"""
Write a Python program to iterate over dictionaries using for loops.
"""

dict1 = {
    "hello": "world",
    "foo": "bar",
    "good": "game",
    "well": "played",
}

for key, value in dict1.items():
    print(f"Key: {key} -> Value: {value}\n")
