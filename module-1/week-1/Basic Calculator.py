# Scratchbook: Simple Calculator - Demonstrating Chapter 1 Concepts from "Automate the Boring Stuff with Python"

# Chapter 1 Concept 1: Printing output to the screen
print("Welcome to the Simple Calculator Scratchbook!")
print("This program demonstrates basic Python concepts from Chapter 1.")

# Chapter 1 Concept 2: Storing values in variables
# Variables are like boxes that hold information we can use later
greeting = "Hello, user!"
print(greeting)

# Chapter 1 Concept 3: Getting input from the user
# The input() function lets us ask the user for information
user_name = input("What's your name? ")
print("Nice to meet you, " + user_name + "!")

# Chapter 1 Concept 4: Working with strings
# Strings are text enclosed in quotes
message = "Let's do some math!"
print(message)

# Chapter 1 Concept 5: Basic math operations
# Python can perform calculations using +, -, *, /, ** (power), // (floor division), % (modulo)
print("Demonstrating basic math:")
a = 10
b = 5
print("a =", a)
print("b =", b)
print("a + b =", a + b)
print("a - b =", a - b)
print("a * b =", a * b)
print("a / b =", a / b)
print("a ** b =", a ** b)  # a to the power of b
print("a // b =", a // b)  # floor division
print("a % b =", a % b)    # modulo (remainder)

# Chapter 1 Concept 6: Converting between data types
# input() returns a string, but we need numbers for math
print("\nNow let's build a simple calculator!")

# Get two numbers from the user (as strings)
num1_str = input("Enter the first number: ")
num2_str = input("Enter the second number: ")

# Convert strings to numbers (floats can handle decimals)
num1 = float(num1_str)
num2 = float(num2_str)

# Get the operation
operation = input("Enter operation (+, -, *, /, **, //, %): ")

# Optional swap for non-commutative operations (division, floor division, modulo, subtraction, exponent)
if operation in ["/", "//", "%", "-", "**"]:
    confirm_swap = input(f"For {operation}, did you mean {num2} {operation} {num1}? (y/n): ")
    if confirm_swap.lower().startswith("y"):
        num1, num2 = num2, num1

# Perform the calculation based on the operation
if operation == "+":
    result = num1 + num2
    print("Result:", num1, "+", num2, "=", result)
elif operation == "-":
    result = num1 - num2
    print("Result:", num1, "-", num2, "=", result)
elif operation == "*":
    result = num1 * num2
    print("Result:", num1, "*", num2, "=", result)
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
        print("Result:", num1, "/", num2, "=", result)
    else:
        print("Error: Cannot divide by zero!")
elif operation == "**":
    result = num1 ** num2
    print("Result:", num1, "**", num2, "=", result)
elif operation == "//":
    if num2 != 0:
        result = num1 // num2
        print("Result:", num1, "//", num2, "=", result)
    else:
        print("Error: Cannot divide by zero!")
elif operation == "%":
    if num2 != 0:
        result = num1 % num2
        print("Result:", num1, "%", num2, "=", result)
    else:
        print("Error: Cannot divide by zero!")
else:
    print("Error: Invalid operation!")

# Chapter 1 Concept 7: Comments
# Comments start with # and are ignored by Python - they're for humans to read
# This scratchbook shows I've learned:
# - How to print messages
# - How to store and use variables
# - How to get input from users
# - How to work with strings and numbers
# - How to perform basic math operations (+, -, *, /, **, //, %)
# - How to convert between data types
# - How to use comments to explain code

print("\nThank you for using the Simple Calculator Scratchbook!")
print("You've seen all the key concepts from Chapter 1 in action.")