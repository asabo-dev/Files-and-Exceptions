# Using Try-Except Block to handle ValueError

num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

try:
    result = int(num1) + int(num2)
    print(f"The result is: {result}")
except ValueError:
    print("Wrong value provided. Enter two numbers.")