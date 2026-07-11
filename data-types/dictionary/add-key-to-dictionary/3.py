"""
Write a Python script to update a dictionary with multiple new keys from a list, setting each to a default value.
"""

new_keys = [2, 3, 4, 5]
sample = {0: 10, 1: 20}
sample.update(dict.fromkeys(new_keys, 0))
print(sample)
