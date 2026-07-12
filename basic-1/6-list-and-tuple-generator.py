"""
Write a Python program that accepts a sequence of comma-separated numbers from the user and generates a list and a tuple of those numbers.
Sample data : 3, 5, 7, 23
Output :
List : ['3', ' 5', ' 7', ' 23']
Tuple : ('3', ' 5', ' 7', ' 23')
"""

user_input = input("Enter comma separated values: ")
input_list = [int(num.strip()) for num in user_input.split(",")]
input_tuple = tuple(input_list)

print(f"List: {input_list}")
print(f"Tuple: {input_tuple}")
