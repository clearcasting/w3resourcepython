"""
Write a Python script to add a new key-value pair to a dictionary only if the key does not exist already.
"""


def add_new(dictionary: dict, key, value) -> None:
    if dictionary.get(key):
        return
    dictionary.update({key: value})


sample = {0: 10, 1: 20}

# This will fail because the key 0 already exists in the dictionary.
print("Attempting to add {0: 30}")
add_new(sample, 0, 30)
print(sample)

# This will succeed because the key 3 does not exist in the dictionary.
print("\nAttempting to add {3: 30}")
add_new(sample, 3, 30)
print(sample)
