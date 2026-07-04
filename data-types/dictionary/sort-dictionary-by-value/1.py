"""
Write a Python script to sort (ascending and descending) a dictionary by value.
"""

data = {
    "two": 2,
    "one": 1,
    "four": 4,
    "three": 3,
}


def sort_dict(data: dict, reverse: bool = False):
    return sorted(data.items(), key=lambda x: x[1], reverse=reverse)


print(f"[*] - Original dictionary order:\n{data}\n")

sorted_dictionary = sort_dict(data)
print(f"[*] - Dictionary sorted ascending:\n{sorted_dictionary}\n")

sorted_dictionary = sort_dict(data, True)
print(f"[*] - Dictionary sorted descending:\n{sorted_dictionary}\n")
