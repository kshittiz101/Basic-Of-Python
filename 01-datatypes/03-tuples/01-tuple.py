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
# third_tuple[0] = 200

# TypeError: 'tuple' object does not support item assignment
# print(third_tuple)

# in python we cannot able to delete individaul element of the tuple, because it is immutable in nature
roles = ("manager", "developer", "graphic designers ")
#  we have to delete the whole tuple
del roles
# print(roles)


# If you want to remove elements
# Convert the tuple to a list, modify it, then convert back:
fruits = ("apples", "orange", "mango", "banana")
print(f"Elements of fruits: {fruits}, and types is {type(fruits)}")

# converting tuples into list
list_of_fruits = list(fruits)
print(type(list_of_fruits))

# here in the list of fruits remove() function will remove first occurance of the friut from list
# remoce work on list not in tuple
list_of_fruits.remove("banana")
print(list_of_fruits)
