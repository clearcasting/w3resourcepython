"""
Write a Python script to merge a list of key-value pairs into an existing dictionary without overwriting existing keys.
"""

sample = {0: 10, 1: 20}
new_values = {0: 30, 1: 40, 2: 30, 3: 40}

for key, value in new_values.items():
    if key not in sample:
        sample[key] = value

print(sample)
