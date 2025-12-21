# In Python, a tuple is a built-in data type used to store a collection of items.
# Tuples are:
# ordered
# immutable
# allows duplication
# allow different data types
# can be create using tuple using ()

# creating tuple
first_tuple = (1, True, "Alex")
print(first_tuple)
print(type(first_tuple))

# tuple with single value
# to create tuple with only one element we have to give comma at last
second_tuple = (20, )
print(second_tuple)
print(type(second_tuple))


# length of the tuple
print(f"Length of the tuple: {len(second_tuple)}")

# access value from tuple
# tuple is collection based datatypes so we can use indexing to access element from tuple
third_tuple = (20, 5, True, "Harry")
print(f"First element: {third_tuple[0]}")

print(f"last element: {third_tuple[-1]}")

# update: we can not update the value of the tuple becausse it is immutable
third_tuple[0] = 200

# TypeError: 'tuple' object does not support item assignment
# print(third_tuple)
