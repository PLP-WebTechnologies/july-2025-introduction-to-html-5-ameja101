# Simple Arithmetic Calculator

# Ask the user to input two numbers and an operation
num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")
operation = input("Enter an operation (+, -, *, /): ")

# Convert the input strings to floats
num1 = float(num1)
num2 = float(num2)

# Perform the operation
if operation == '+':
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")

elif operation == '-':
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")

elif operation == '*':
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
elif operation == '/':
    if num2 != 0:
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operation. Please enter one of +, -, *, or /.")
