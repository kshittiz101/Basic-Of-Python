#  list comprehension
# syntax
# [expression for item in iterable if condition]

# traditional way to create list of squares
squares = []
for x in range(10):
    squares.append(x**2)

print(f'From Using traditional ways: {squares}')

# list comprehension way to create list of squares
squares = [x**2 for x in range(10)]
print(f'From Using list conprehension ways: {squares}')


# list comprehension way
# filter only even squares
even_squares = [x**2 for x in range(10) if x % 2 == 0]
print(f"Squares of even number only: {even_squares}")


# using if else in conprehension
# if x is even the square it else keep it as it is
result = [x**2 if x % 2 == 0 else x for x in range(10)]
print(result)


# 1. squares of only even number upto 1 to 20
square_of_evens = [x**2 for x in range(1, 21) if x % 2 == 0]
print(square_of_evens)


# Question 2: Uppercase Long Names
# Task: Given a list of names, create a new list with names converted to UPPERCASE,
# but only if the name has more than 4 letters.

# Input: ["sam", "john", "alexander", "max", "elizabeth"]
# Expected Output: ['ALEXANDER', 'ELIZABETH']

names = ["sam", "john", "alexander", "max", "elizabeth"]
# Filter length > 4, transform to .upper()
result = [name.upper() for name in names if len(name) > 4]
print(result)


# Question 3: Cleaning Data (The if-else Transform)
# Task: Given a list of numbers, create a new list where:

# If the number is positive, square it.
# If the number is negative, replace it with 0.
# Note: This requires placing the if/else BEFORE the loop.
# Input: [5, -2, 10, -8, 3]
# Expected Output: [25, 0, 100, 0, 9]

numbers = [5, -2, 10, -8, 3]
final_value = [num**2 if num > 0 else 0 for num in numbers]
print(final_value)
