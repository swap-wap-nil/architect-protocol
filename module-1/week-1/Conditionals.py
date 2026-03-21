# Chapter 2 Scratchbook - Automate the Boring Stuff (Python)
# Topics: Boolean values, comparison, if, elif, else, while, for, break, continue, range, truthiness, try/except

print("Chapter 2 Scratchbook: Flow control & decisionmaking")

# 1) Boolean values and comparison operators
print("\n1) Boolean values / comparisons")
a = 42
b = 100
print(f"{a} == {b}", a == b)
print(f"{a} != {b}", a != b)
print(f"{a} < {b}", a < b)
print(f"{a} <= {b}", a <= b)
print(f"{a} > {b}", a > b)
print(f"{a} >= {b}", a >= b)

# 2) Logical operators: and, or, not
print("\n2) Logical operators")
x = True
y = False
print(f"{x} and {y}:", x and y)
print(f"{x} or {y}:", x or y)
print(f"not {x}:", not x)

# 3) if, elif, else
print("\n3) if / elif / else")
age = int(input("Enter your age: "))
if age < 0:
    print("Age cannot be negative")
elif age < 13:
    print("Child")
elif age < 20:
    print("Teenager")
elif age < 65:
    print("Adult")
else:
    print("Senior")

# 4) Truthiness of values
print("\n4) Truthiness examples")
samples = [0, 1, "", "hello", [], [1], None, {}, {"k": 1}]
for v in samples:
    print(repr(v), "is", bool(v))

# 5) while loop
print("\n5) while loop: guessing game")
secret = 7
guess = None
count = 0
while guess != secret and count < 5:
    guess = int(input("Guess number 1-10: "))
    count += 1
    if guess < secret:
        print("Too low")
    elif guess > secret:
        print("Too high")
    else:
        print("Correct!")
        break
else:
    if guess != secret:
        print("No more tries")

# 6) for loop with range
print("\n6) for loop with range and summation")
total = 0
for i in range(1, 11):           # 1..10
    total += i
    if i == 5:
        continue                  # skip extra work for example
    if i == 9:
        break                     # demonstrate break usage
print("Partial total after break:", total)

# 7) nested loops
print("\n7) nested loops: multiplication table")
for row in range(1, 6):
    for col in range(1, 6):
        print(f"{row*col:3}", end=" ")
    print()

# 8) try/except for control flow on errors
print("\n8) try/except")
val = input("Enter integer to divide 100 by: ")
try:
    n = int(val)
    print("100 /", n, "=", 100/n)
except ValueError:
    print("You need to enter a valid integer.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
finally:
    print("End of chapter 2 exercise")

# 9) small function + conditional combinatorics
print("\n9) function with conditional logic")
def is_leap_year(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    return year % 4 == 0

for year in (1900, 2000, 2004, 2019, 2024):
    print(year, "leap:", is_leap_year(year))