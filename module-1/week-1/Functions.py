# Exploring functions in Python

# Creating a magic8 ball

import random

def get_answer(answer_number):
    # Returns a fortune answer based on what int answer_number is, 1 to 9
  if answer_number == 1:
        return 'It is certain'
  elif answer_number == 2:
        return 'It is decidedly so'
  elif answer_number == 3:
        return 'Yes'
  elif answer_number == 4:
        return 'Reply hazy try again'
  elif answer_number == 5:
        return 'Ask again later'
  elif answer_number == 6:
        return 'Concentrate and ask again'
  elif answer_number == 7:
        return 'My reply is no'
  elif answer_number == 8:
        return 'Outlook not so good'
  elif answer_number == 9:
        return 'Very doubtful'

print('Ask a yes or no question:')
input('>')
print(get_answer(random.randint(1, 9)))


# Code for 100 coin flips
# understanding named arguments and default values in functions

import random
for i in range(100):  # Perform 100 coin flips.
    if random.randint(0, 1) == 0:
        print('H', end=' ')
    else:
        print('T', end=' ')
print()  # Print one newline at the end.

# passing multiple values to trigger a space separation by default in print() function

print('Hello','World','Python','is','fun!')

print('Hello','World','Python','is','fun!', sep='-')  # Using a different separator

# Understanding the CallStack and how functions call other functions

def a():
    print('a() starts')
    b()
    d()
    print('a() returns')

def b():
    print('b() starts')
    c()
    print('b() returns')

def c():
    print('c() starts')
    print('c() returns')

def d():
    print('d() starts')
    print('d() returns')

a()


# Understanding the scope of variables in functions

def spam():
    eggs = 'spam local'
    print(eggs)  # This will print 'spam local'
eggs = 'global'
spam()
print(eggs)  # This will print 'global'

# Understanding the global keyword to modify global variables inside a function

def spam():
      global eggs
      eggs = 'spam global'
      print(eggs)  # This will print 'spam global'
eggs = 'global'
spam()      
print(eggs)  # This will also print 'spam global' because we modified the global variable inside the function

# Understanding the difference between local and global variables with the same name
def spam():
  global eggs
  eggs = 'spam'  # This is the global variable.

def bacon():
  eggs = 'bacon'  # This is a local variable.

def ham():
  print(eggs)  # This is the global variable.

eggs = 'global'  # This is the global variable.
spam()
print(eggs) # this will print 'spam' because the global variable was modified by the spam() function



# Exception handling in functions using try/except blocks

def spam(divide_by):
    try:
        # Any code in this block that causes ZeroDivisionError won't crash the program:
        return 42 / divide_by
    except ZeroDivisionError:
        # If ZeroDivisionError happened, the code in this block runs:
        print('Error: Invalid argument.')

print(spam(2))
print(spam(12))
print(spam(0)) # This will print Error: Invalid argument. because of the try/except block handling the ZeroDivisionError
print(spam(1))

# demontrating error in the try block calls the except block and the rest of the code in the try block is not executed after the error occurs

def spam(divide_by):
    return 42 / divide_by

try:
    print(spam(2))
    print(spam(12))
    print(spam(0))
    print(spam(1))
except ZeroDivisionError:
    print('Error: Invalid argument.')


# Zigzag pattern printing using functions

import time, sys
indent = 0  # How many spaces to indent
indent_increasing = True  # Whether the indentation is increasing or not

try:
    while True:  # The main program loop
        print(' ' * indent, end='')
        print('********')
      #   time.sleep(0.1) # Pause for 1/10th of a second.

        if indent_increasing:
            # Increase the number of spaces:
            indent = indent + 1
            if indent == 20:
                # Change direction:
                indent_increasing = False
        else:
            # Decrease the number of spaces:
            indent = indent - 1
            if indent == 0:
                # Change direction:
                indent_increasing = True
except KeyboardInterrupt:
    sys.exit()


# Spike - a function that prints a spike pattern

import time, sys

try:
    while True:  # The main program loop
        # Draw lines with increasing length:
        for i in range(1, 9):
            print('-' * (i * i))
            time.sleep(0.1)

        # Draw lines with decreasing length:
        for i in range(7, 1, -1):
            print('-' * (i * i))
            time.sleep(0.1)
except KeyboardInterrupt:
    sys.exit()


# Collatz Conjecture Function
# The Collatz conjecture is a famous unsolved problem in mathematics
# It states that for any positive integer n, if you repeatedly apply these rules:
# - If n is even, divide it by 2
# - If n is odd, multiply by 3 and add 1
# You will eventually reach 1

def collatz(number):
    """
    Takes a positive integer and applies the Collatz conjecture rules.
    Prints each step of the sequence until it reaches 1.
    
    Args:
        number (int): A positive integer to start the sequence with
    """
    # Keep track of the current number in the sequence
    current = number
    
    # Continue the sequence until we reach 1
    while current != 1:
        print(current)  # Print the current number
        
        # Check if current number is even
        if current % 2 == 0:
            # If even, divide by 2
            current = current // 2
        else:
            # If odd, multiply by 3 and add 1
            current = 3 * current + 1
    
    # Print the final 1
    print(current)

# Example usage of the Collatz function
print("Collatz sequence for 3:")
collatz(3)

print("\nCollatz sequence for 7:")
collatz(7)

# Interactive Collatz sequence with user input
print("\n" + "="*50)
print("Interactive Collatz Conjecture Calculator")
print("="*50)

while True:
    try:
        # Get user input
        user_input = input("Enter a positive integer (or 'quit' to exit): ")
        
        # Check if user wants to quit
        if user_input.lower() == 'quit':
            print("Thanks for using the Collatz calculator!")
            break
        
        # Convert input to integer
        number = int(user_input)
        
        # Validate that it's a positive integer
        if number <= 0:
            print("Please enter a positive integer greater than 0.")
            continue
        
        # Run the Collatz sequence
        print(f"\nCollatz sequence for {number}:")
        collatz(number)
        print()  # Add blank line for readability
        
    except ValueError:
        # Handle non-integer input
        print("Invalid input. Please enter a positive integer or 'quit' to exit.")
    except KeyboardInterrupt:
        # Handle Ctrl+C to exit gracefully
        print("\n\nProgram interrupted. Goodbye!")
        break


   