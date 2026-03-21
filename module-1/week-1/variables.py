# Python Variables Scratchbook

# 1. Creating and assigning variables
name = "Alice"
age = 25
height = 5.9
is_student = True

print(name)
print(age)
print(height)
print(is_student)

# 2. Variable naming conventions
my_variable = 10
myVariable = 20  # camelCase (less common in Python)
MY_CONSTANT = 100  # UPPER_CASE for constants
_private_var = 5  # underscore prefix suggests private

# 3. Multiple assignment
x, y, z = 1, 2, 3
print(x, y, z)

# 4. Swapping variables
a = 5
b = 10
a, b = b, a
print(f"a: {a}, b: {b}")

# 5. Type checking
print(type(name))
print(type(age))
print(type(is_student))

# 6. Updating variables
counter = 0
counter = counter + 1
counter += 1
print(counter)

# 7. Input and output
name = input("What is your name? ")
age = int(input("How old are you? "))
fav = int(input("Your favorite number? "))

print(f"Hi, {name}!")
print(f"Next year you will be {age + 1}.")
print(f"Ten times your favorite number is {fav * 10}.")

# 8. Time calculation
h = int(input("Hours: "))
m = int(input("Minutes: "))
s = int(input("Seconds: "))

total = h * 3600 + m * 60 + s
print(f"Total seconds: {total}")

if total < 86400:
    print("This is less than one day.")
else:
    print("This is one day or more.")


