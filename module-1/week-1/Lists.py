# Chapter 4: Lists Scratchpad from "Automate the Boring Stuff with Python"
# This file contains examples and exercises from Chapter 4 on Lists.

# The List Data Type
# Lists are ordered sequences of values, enclosed in square brackets [].

# Example: Creating a list
spam = ['cat', 'bat', 'rat', 'elephant']
print("List spam:", spam)

# Getting Individual Values in a List with Indexes
# Indexes start at 0.
print("spam[0]:", spam[0])  # 'cat'
print("spam[1]:", spam[1])  # 'bat'
print("spam[2]:", spam[2])  # 'rat'
print("spam[3]:", spam[3])  # 'elephant'

# Negative Indexes
# Negative indexes start from the end.
print("spam[-1]:", spam[-1])  # 'elephant'
print("spam[-2]:", spam[-2])  # 'rat'

# Getting Sublists with Slices
# Slices return a new list.
print("spam[0:4]:", spam[0:4])  # ['cat', 'bat', 'rat', 'elephant']
print("spam[1:3]:", spam[1:3])  # ['bat', 'rat']
print("spam[0:-1]:", spam[0:-1])  # ['cat', 'bat', 'rat']
print("spam[:2]:", spam[:2])  # ['cat', 'bat']
print("spam[1:]:", spam[1:])  # ['bat', 'rat', 'elephant']
print("spam[:]:", spam[:])  # ['cat', 'bat', 'rat', 'elephant']

# Getting a List’s Length with len()
print("len(spam):", len(spam))  # 4

# Changing Values in a List with Indexes
spam[1] = 'aardvark'
print("After spam[1] = 'aardvark':", spam)  # ['cat', 'aardvark', 'rat', 'elephant']

# List Concatenation and List Replication
print("[1, 2, 3] + ['A', 'B', 'C']:", [1, 2, 3] + ['A', 'B', 'C'])  # [1, 2, 3, 'A', 'B', 'C']
print("['X', 'Y', 'Z'] * 3:", ['X', 'Y', 'Z'] * 3)  # ['X', 'Y', 'Z', 'X', 'Y', 'Z', 'X', 'Y', 'Z']

# Removing Values from Lists with del Statements
del spam[2]
print("After del spam[2]:", spam)  # ['cat', 'aardvark', 'elephant']

# Working with Lists
# Using for Loops with Lists
supplies = ['pens', 'staplers', 'flame-throwers', 'binders']
for i in range(len(supplies)):
    print('Index', i, 'in supplies is:', supplies[i])

# The in and not in Operators
print("'howdy' in ['hello', 'hi', 'howdy', 'heyas']:", 'howdy' in ['hello', 'hi', 'howdy', 'heyas'])  # True
print("'cat' in spam:", 'cat' in spam)  # True

# The Multiple Assignment Trick
cat = ['fat', 'orange', 'loud']
size, color, disposition = cat
print("size:", size, "color:", color, "disposition:", disposition)

# Swapping values
a, b = 'Alice', 'Bob'
a, b = b, a
print("a:", a, "b:", b)

# Augmented Assignment Operators
spam = [1, 2, 3]
spam += ['A', 'B', 'C']
print("spam after +=:", spam)  # [1, 2, 3, 'A', 'B', 'C']

bacon = ['Zophie']
bacon *= 3
print("bacon after *= 3:", bacon)  # ['Zophie', 'Zophie', 'Zophie']

# Methods
# Finding a Value in a List with the index() Method
spam = ['hello', 'hi', 'howdy', 'heyas']
print("spam.index('hello'):", spam.index('hello'))  # 0

# Adding Values to Lists with the append() and insert() Methods
spam = ['cat', 'dog', 'bat']
spam.append('moose')
print("spam after append('moose'):", spam)  # ['cat', 'dog', 'bat', 'moose']

spam.insert(1, 'chicken')
print("spam after insert(1, 'chicken'):", spam)  # ['cat', 'chicken', 'dog', 'bat', 'moose']

# Removing Values from Lists with remove()
spam.remove('bat')
print("spam after remove('bat'):", spam)  # ['cat', 'chicken', 'dog', 'moose']

# Sorting the Values in a List with the sort() Method
spam = [2, 5, 3.14, 1, -7]
spam.sort()
print("spam after sort():", spam)  # [-7, 1, 2, 3.14, 5]

spam = ['ants', 'cats', 'dogs', 'badgers', 'elephants']
spam.sort()
print("spam after sort():", spam)  # ['ants', 'badgers', 'cats', 'dogs', 'elephants']

spam.sort(reverse=True)
print("spam after sort(reverse=True):", spam)  # ['elephants', 'dogs', 'cats', 'badgers', 'ants']

# Example Program: Magic 8 Ball with a List
import random

messages = ['It is certain',
    'It is decidedly so',
    'Yes definitely',
    'Reply hazy try again',
    'Ask again later',
    'Concentrate and ask again',
    'My reply is no',
    'Outlook not so good',
    'Very doubtful']

print("Ask a yes or no question:")
input('> ')
print("Magic 8 Ball says:", messages[random.randint(0, len(messages) - 1)])

# List-like Types: Strings and Tuples
# Strings can be treated like lists of characters.
name = 'Zophie'
print("name[0]:", name[0])  # 'Z'
print("'Zo' in name:", 'Zo' in name)  # True'

# Mutable and Immutable Data Types
# Lists are mutable, strings are immutable.
# Trying to change a string character will error.
# name[0] = 'C'  # TypeError

# The Tuple Data Type
# Tuples are immutable lists, enclosed in parentheses ().
eggs = ('hello', 42, 0.5)
print("eggs[0]:", eggs[0])  # 'hello'
# eggs[1] = 99  # TypeError

# Converting Types with the list() and tuple() Functions
print("tuple(['cat', 'dog', 5]):", tuple(['cat', 'dog', 5]))  # ('cat', 'dog', 5)
print("list(('cat', 'dog', 5)):", list(('cat', 'dog', 5)))  # ['cat', 'dog', 5]
print("list('hello'):", list('hello'))  # ['h', 'e', 'l', 'l', 'o']

# References
# Variables store references to lists, not the lists themselves.
spam = [0, 1, 2, 3, 4, 5]
cheese = spam
cheese[1] = 'Hello!'
print("spam:", spam)  # [0, 'Hello!', 2, 3, 4, 5]
print("cheese:", cheese)  # [0, 'Hello!', 2, 3, 4, 5]

# Passing References
def eggs(someParameter):
    someParameter.append('Hello')

spam = [1, 2, 3]
eggs(spam)
print("spam after passing to eggs():", spam)  # [1, 2, 3, 'Hello']

# The copy Module’s copy() and deepcopy() Functions
import copy
spam = ['A', 'B', 'C', 'D']
cheese = copy.copy(spam)
cheese[1] = 42
print("spam:", spam)  # ['A', 'B', 'C', 'D']
print("cheese:", cheese)  # ['A', 42, 'C', 'D']

# Practice Questions (Answers in comments)
# 1. [] is an empty list.
# 2. spam[2] = 'hello'
# 3. spam[int(int('3' * 2) // 11)] = spam[int(33 // 11)] = spam[3] = 'd'
# 4. 'd'
# 5. ['a', 'b']
# 6. 1
# 7. [3.14, 'cat', 11, 'cat', True, 99]
# 8. [3.14, 11, 'cat', True]
# 9. + for concatenation, * for replication
# 10. append() adds to the end, insert() adds at a specific index
# 11. del statement and remove() method
# 12. Indexing, slicing, len(), in/not in, for loops
# 13. Lists are mutable, tuples are immutable
# 14. (42,)
# 15. tuple(list_value), list(tuple_value)
# 16. References to the list values
# 17. copy() copies the list, deepcopy() copies nested lists too

# Practice Projects

# Comma Code
def comma_code(list_value):
    if len(list_value) == 0:
        return ''
    elif len(list_value) == 1:
        return str(list_value[0])
    else:
        return ', '.join(str(item) for item in list_value[:-1]) + ', and ' + str(list_value[-1])

spam = ['apples', 'bananas', 'tofu', 'cats']
print("Comma code result:", comma_code(spam))

# Character Picture Grid
grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

for y in range(len(grid[0])):
    for x in range(len(grid)):
        print(grid[x][y], end='')
    print()

# Coin Flip Streaks Program
# This program simulates 10,000 experiments of 100 coin flips each,
# checking for streaks of 6 heads or 6 tails in a row.

import random

numberOfStreaks = 0

for experimentNumber in range(10000):
    # Generate a list of 100 'H' or 'T' values.
    flips = []
    for i in range(100):
        if random.randint(0, 1) == 0:
            flips.append('H')
        else:
            flips.append('T')
    
    # Check for streaks of 6 in a row.
    streak = 1
    for i in range(1, len(flips)):
        if flips[i] == flips[i-1]:
            streak += 1
            if streak == 6:
                numberOfStreaks += 1
                break
        else:
            streak = 1

print('Chance of streak: %s%%' % (numberOfStreaks / 100))

# Additional: Matrix Screensaver Simulation using Lists
# This is a simple simulation of the Matrix screensaver using lists to represent columns of falling characters.

import random, sys, time

WIDTH = 70  # The number of columns

try:
    # For each column, when the counter is 0, no stream is shown.
    # Otherwise, it acts as a counter for how many times a 1 or 0
    # should be displayed in that column.
    columns = [0] * WIDTH
    while True:
        # Loop over each column:
        for i in range(WIDTH):
            if random.random() < 0.02:
                # Restart a stream counter on this column.
                # The stream length is between 4 and 14 characters long.
                columns[i] = random.randint(4, 14)

            # Print a character in this column:
            if columns[i] == 0:
                # Change this ' '' to '.' to see the empty spaces:
                print(' ', end='')
            else:
                # Print a 0 or 1:
                print(random.choice([0, 1]), end='')
                columns[i] -= 1  # Decrement the counter for this column.
        print()  # Print a newline at the end of the row of columns.
        time.sleep(0.1)  # Each row pauses for one tenth of a second.
except KeyboardInterrupt:
    sys.exit()  # When Ctrl-C is pressed, end the program.


