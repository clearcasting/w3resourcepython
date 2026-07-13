"""
Write a Python program that accepts a filename from the user and prints the extension of the file.
Sample filename : abc.java
Output : java
"""

user_input = input("Enter a filename (with extension): ").strip()
if "." in user_input:
    extension = user_input.split(".")[-1]
    print(extension)
else:
    print("No extension found.")
