# set comprehensions
# it is a concise and readable way to create a set in python.
# just like the list comprehensions, the set comprehensions will create set
# which means the resulting collection is set that means unique and unordered elements

# syntax:
# unlike the list comprehension use [] brackets, whereas set comprehension use set comprehension
# {expressions for item in iterable}

list_of_books = [
    "code with python", 'Python Fundamentals',
    'Clean Code', 'code with python', 'learn how to learn',
    'clean code'
]
converts_uppercase_books = [book.upper() for book in list_of_books]
unique_values = {book for book in converts_uppercase_books}
print(unique_values)


list_of_books = [
    "code with python", 'Python Fundamentals',
    'Clean Code', 'code with python', 'learn how to learn',
    'clean code'
]
unique_values = {book.upper() for book in list_of_books}
print(unique_values)
