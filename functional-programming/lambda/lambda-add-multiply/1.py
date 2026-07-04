"""
Write a Python program to create a lambda function that adds 15 to a given number passed in as an argument, also create a lambda function that multiplies argument x with argument y and prints the result.

Sample Output:
25
48
"""

# lambda arguments: expression
user_input = int(input("[*] - Enter a number to add 15 to it: "))
add_15 = lambda arg: arg + 15
print(add_15(user_input))

print("\n[*] - The program will now multiply two numbers of your choosing.")
num1 = int(input("[*] - Enter number a: "))
num2 = int(input("[*] - Enter number b: "))
multiply = lambda a, b: a * b
print(multiply(num1, num2))
